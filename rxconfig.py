import reflex as rx

config = rx.Config(
    show_built_with_reflex=False,
    app_name="reflex_viaje",
    backend_port=8001,
    cors_allowed_origins=[
        "https://reflex.inimonizango.eu",
        "https://inimonizango.eu",
        "https://api.inimonizango.eu",
        "http://localhost:3000",
    ],
    api_url="https://api.inimonizango.eu",
    deploy_url="https://reflex.inimonizango.eu",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)