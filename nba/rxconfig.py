import reflex as rx

config = rx.Config(
    app_name="nba",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
