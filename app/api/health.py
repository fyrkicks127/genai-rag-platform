from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    result = {}
    result['status'] = 'Ok'
    result['service'] = 'Genai-Rag-Platform'
    return result
