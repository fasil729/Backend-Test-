from app.db.base_class import Base  # This imports the Base class to use in your models
from app.models.user import User
from app.models.post import Post

# Include all models in Base for Alembic to detect them
