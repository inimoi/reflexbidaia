from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import create_client, Client
from pydantic import BaseModel, EmailStr, Field, field_validator
import os
from dotenv import load_dotenv

load_dotenv()

# Crear cliente de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Esquema de seguridad
security = HTTPBearer()

# ==================== MODELOS ====================

class Register(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    name: str = Field(..., min_length=5)

    @field_validator("password")
    @classmethod
    def password_complexity(cls, v: str) -> str:
        if not any(char.isdigit() for char in v):
            raise ValueError("La contraseña debe contener al menos un número")
        if not any(char.isupper() for char in v):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula")
        return v

class Login(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)

class Token(BaseModel):
    access_token: str
    token_type: str
    user: dict

class UserProfile(BaseModel):
    id: str
    email: str
    user_metadata: dict = None
    
    class Config:
        from_attributes = True

# ==================== FUNCIONES DE AUTENTICACIÓN ====================

async def register_user(email: str, password: str, name: str = None) -> dict:
    """
    Registrar un nuevo usuario en Supabase Auth
    """
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {
                    "name": name or email.split("@")[0],
                    "email": email
                }
            }
        })
        
        if response.user:
            return {
                "user": response.user,
                "session": response.session
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error al registrar el usuario"
            )
    
    except Exception as e:
        error_message = str(e)
        if "already registered" in error_message or "User already exists" in error_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {error_message}"
        )
    


async def login_user(email: str, password: str) -> dict:
    """
    Iniciar sesión en Supabase Auth
    """
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        
        if response.session:
            return {
                "user": response.user,
                "session": response.session,
                "access_token": response.session.access_token
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o contraseña incorrectos"
            )
    
    except Exception as e:
        error_message = str(e)
        if "Invalid login credentials" in error_message:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o contraseña incorrectos"
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {error_message}")


async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Valida un token usando Supabase Auth
    """
    token = credentials.credentials
    try:
        # Supabase valida el token automáticamente
        user = supabase.auth.get_user(token)
        
        return {
            "valid": True,
            "user_id": user.user.id,
            "email": user.user.email,
            "user": user.user.model_dump()
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido: {str(e)}"
        )
    

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verificar el token de acceso y obtener el usuario actual
    """
    token = credentials.credentials
    
    try:
        # Verificar el token con Supabase
        user = supabase.auth.get_user(token)
        
        if user and user.user:
            return user.user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se pudo validar las credenciales"
            )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )