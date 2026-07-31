from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schema.upload import UploadResponse
from app.services.ingestion_service import IngestionService

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

service = IngestionService()


@router.post("/", response_model=UploadResponse)
async def upload_document(
    file: UploadFile = File(...)
):

    suffix = Path(file.filename).suffix.lower()

    if suffix not in [".pdf", ".docx", ".txt"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks = service.ingest(str(file_path))

    return UploadResponse(
        filename=file.filename,
        chunks=chunks,
        message="Document indexed successfully."
    )