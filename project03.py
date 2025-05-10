import streamlit as st
from datetime import date

# 비밀번호 설정
correct_password = "0124"

# 로그인 상태 초기화
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# 로그인 함수
def login():
    password = st.text_input("비밀번호를 입력하세요", type="password")
    if st.button("로그인"):
        if password == correct_password:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("비밀번호가 틀렸습니다.")

# 로그인 페이지
if not st.session_state["authenticated"]:
    st.title("🔐 로그인")
    login()

else:
    class Nasdaq:
        registry = []

        def __init__(self, name, wantcost, purpose, earnings_date=None):
            self.name = name 
            self.wantcost = wantcost
            self.purpose = purpose
            self.earnings_date = earnings_date
            Nasdaq.registry.append(self)

        def show(self):
            st.write(f"💰 **{self.name}**의 매수 희망 가격: **{self.wantcost} 달러**")

        def purposesell(self):
            st.write(f"📈 **{self.name}**의 목표 매도 가격: **{self.purpose} 달러**")

        def show_earnings_date(self):
            if self.earnings_date:
                days_left = (self.earnings_date - date.today()).days
                if days_left >= 0:
                    st.write(f"🗓️ **{self.name}**의 다음 실적 발표일: {self.earnings_date.strftime('%Y-%m-%d')} (D-{days_left})")
                else:
                    st.write(f"📉 **{self.name}**의 실적 발표일({self.earnings_date.strftime('%Y-%m-%d')})이 이미 지났습니다.")
            else:
                st.write(f"❌ **{self.name}**의 실적 발표일 정보가 없습니다.")

        @staticmethod
        def find_by_name(name):
            for stock in Nasdaq.registry:
                if stock.name == name:
                    return stock
            return None

    # 종목 초기화
    if not Nasdaq.registry:
        Nasdaq("테슬라", 280, 300, date(2025, 7, 23))
        Nasdaq("애플", 197, 250, date(2025, 8, 1))
        Nasdaq("엔비디아", 117, 200, date(2025, 5, 29))

    # 페이지 선택
    page = st.sidebar.radio("페이지를 선택하세요", ["📘 종목 조회", "📄 보유 종목 리스트", "📚 번외"])

    if page == "📘 종목 조회":
        st.title("📊 나스닥 종목 정보 조회")
        stock_name = st.text_input("종목명을 입력하세요 (예: 테슬라, 애플, 엔비디아)")
        if stock_name:
            stock = Nasdaq.find_by_name(stock_name.strip())
            if stock:
                stock.show()
                stock.purposesell()
                stock.show_earnings_date()
            else:
                st.warning("저장된 정보가 존재하지 않습니다. 정확한 종목명을 입력해주세요.")

    elif page == "📄 보유 종목 리스트":
        st.title("📋 보유 중인 종목 리스트")
        for stock in Nasdaq.registry:
            st.markdown(f"- **{stock.name}**")

    elif page == "📚 번외":
        st.title("📚 번외 페이지")
        st.write("✅ 강민철의 기출분석")
        st.write("✅ 양승진 기출코드")
        st.write("✅ 믿어봐 글 편")
        
        # 이미지 표시
        st.image("kang.png", use_container_width=True)

