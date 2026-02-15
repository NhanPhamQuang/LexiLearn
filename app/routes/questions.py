from fastapi import APIRouter, Depends, HTTPException
from app.database import question_collection
from app.models import Question
from app.schemas import QuestionCreate
from app.routes.auth import admin_required
from app.auth import get_current_user
from datetime import datetime

router = APIRouter()

@router.post("/questions")
async def create_question_api(
    question_data: QuestionCreate,
    user: dict = Depends(get_current_user)
):
    # Verify admin
    admin_required(user)

    # Create model instance
    question = Question(
        **question_data.dict(),
        created_at=datetime.utcnow().isoformat()
    )

    # Insert into DB
    result = await question_collection.insert_one(question.dict())

    return {
        "id": str(result.inserted_id),
        "message": "Question created successfully"
    }
