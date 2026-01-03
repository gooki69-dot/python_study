import oracledb

# 접속 정보 설정
USER = "sportsbook"
PASSWORD = "Bk0330Q0715"
DSN = "lab"  # 호스트:포트/서비스이름

try:
    # 1. 연결 생성 (Thin 모드)
    connection = oracledb.connect(user=USER, password=PASSWORD, dsn=DSN)

    # 2. 커서 생성
    cursor = connection.cursor()

    # 3. SQL 실행
    cursor.execute("SELECT * FROM baseball where season_code = 'SS01012025'")  
    #
    # 4. 결과 가져오기
    for row in cursor:
        print(row)

except oracledb.Error as e:
    print(f"오류 발생: {e}")

finally:
    # 5. 연결 종료 (반드시 필요)
    if 'connection' in locals():
        connection.close()
