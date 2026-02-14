from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from fastapi import Request, HTTPException, status
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.database import user_collection


# =========================
# Password Hashing Setup
# =========================

# Sử dụng bcrypt để hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash password trước khi lưu vào database
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    So sánh password nhập vào với password đã hash
    """
    return pwd_context.verify(plain_password, hashed_password)


# =========================
# JWT Token
# =========================

def create_access_token(data: dict) -> str:
    """
    Tạo JWT token
    - data phải chứa ít nhất: sub (email)
    - Có thể chứa role
    - Tự động thêm exp (expire time)
    """
    to_encode = data.copy()

    # Thêm thời gian hết hạn
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Encode thành JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# =========================
# Get Current User (Dependency)
# =========================

async def get_current_user(request: Request):
    """
    Lấy user hiện tại từ cookie:
    1. Lấy access_token từ cookie
    2. Decode JWT
    3. Tìm user trong database
    4. Trả về user (không chứa hashed_password)
    """

    # Lấy token từ cookie
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    try:
        # Decode JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email: str = payload.get("sub")
        role: str = payload.get("role")

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    # Tìm user trong DB
    user = await user_collection.find_one({"email": email})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    # Trả về user sạch (không lộ hashed_password)
    return {
        "email": user["email"],
        "full_name": user.get("full_name"),
        "role": user.get("role", "user")
    }
