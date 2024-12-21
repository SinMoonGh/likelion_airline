import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import pytest
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from fast_api.user.models import User, Base
from fast_api.user.database import Database

@pytest.fixture
def db_engine():
    """데이터베이스 엔진 생성"""
    database = Database()
    try:
        engine = database.get_engine()
        yield engine
        engine.dispose()  # 테스트 후 연결 해제
    except Exception as e:
        pytest.fail(f"데이터베이스 연결 실패: {e}")


def test_connection_db(db_engine):
    """데이터베이스 연결 테스트"""
    assert db_engine is not None, "엔진 생성 실패"
    connection = None
    try:
        connection = db_engine.connect()
        assert connection is not None, "데이터베이스 연결 실패"
        print("데이터베이스 연결 성공")
    finally:
        if connection:
            connection.close()


@pytest.fixture
def test_db_session():
    """세션 생성"""
    try:
        database = Database()
        session = database.get_session()
        yield session
        session.rollback()
        session.close()
    except Exception as e:
        pytest.fail(f"세션 생성 실패: {e}")


def test_session_creation(test_db_session):
    """세션 생성 테스트"""
    assert test_db_session is not None, "세션 생성 실패"
    print("세션 생성 성공")


@pytest.fixture
def test_engine():
    """테스트용 엔진 생성"""
    database = Database()
    engine = database.get_engine()
    yield engine
    engine.dispose()  # 테스트 후 연결 해제


def test_create_tables(test_engine):
    """테이블 생성 테스트"""
    # 테이블 생성
    Base.metadata.create_all(test_engine)
    
    # 데이터베이스에 생성된 테이블 목록 가져오기
    inspector = inspect(test_engine)
    tables = inspector.get_table_names()
    
    # 테스트: 특정 테이블이 존재하는지 확인
    expected_tables = ["users"]  # 생성하려는 테이블 이름
    for table in expected_tables:
        assert table in tables, f"테이블 '{table}' 생성 실패"
    print("테이블 생성 성공:", tables)


def test_insert_airline(test_db_session: Session):
    """데이터베이스에 데이터 삽입 테스트"""
    new_data = User(firstName = "홍", lastName = "길동", email="ddd@naver.com", password="1111")
    test_db_session.add(new_data)
    test_db_session.commit()
    
    # 데이터가 삽입되었는지 확인
    inserted_airline = test_db_session.query(User).filter_by(lastName="길동").first()
    assert inserted_airline is not None, "데이터 삽입 실패"
    assert inserted_airline.last_name == "길동", "데이터 필드 값 불일치"
    print("데이터 삽입 성공")
    

