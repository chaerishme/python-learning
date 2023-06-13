import tkinter as tk
import random

# 단어 그룹 설정
word_groups = {
    "행정": ['행정', '신공공관리론', '뉴거버넌스론', '공공가치관리론', '넛지이론', '정책', '구성정책', '공식적 참여자', '합리 모형', '정책 집행', '통합 모형', '총괄 평가', '과정 평가', '정책 대체', '정책 종결', '정책 갈등', '행정 조직', '관료제론', '과잉동조', '목표 대치'],
    "정치": ['관료제', '국가원수', '권위주의체제', '대리인모델', '신탁인모델', '민주주의', '베스트팔렌조약', '비례대표제', '사회운동', '성문법', '소선거구 단순다수제', '신자유주의', '위헌심판', '이데올로기', '이익집단', '정당일체감', '정통성', '지대', '쿠데타', '포퓰리즘'],
    "경제": ['경제주체', '시장경제체제', '혼합경제체제', '탄력성', '소비자잉여', '한계비용', '독과점', '규모의 경제', '역선택', '도덕적 해이', '임금', '지대', '노동조합', '최고가격제', '투기', '조세', '소득분배', '명목소득', '디플레이션 갭', '보호무역'],
    "사회복지": ['클라이언트', '라포', '복지국가', '사회부조', '사회보험', '사회복지행정', '지역복지', '국제사회복지', '아동복지', '노인복지', '장애인복지', '정신건강사회복지', '교정복지', '사례관리']
}

current_word_group = []  # 현재 선택된 단어 그룹
current_word_index = 0  # 현재 표시되고 있는 단어 인덱스
correct_count = 0  # 정확히 입력한 개수
total_count = 0  # 총 입력한 개수
wrong_words = []


def hide_radio_selection():
    for widget in window.winfo_children():
        if isinstance(widget, tk.Radiobutton):
            widget.pack_forget()

# 이서빈
def start_game():
    global current_word_group, current_word_index, correct_count, total_count
    
    # 선택한 단어 그룹 설정
    selected_group = word_group_var.get()
    current_word_group = word_groups[selected_group]
    random.shuffle(current_word_group)  # 단어 그룹을 랜덤하게 섞기

    # 게임 시작 전에 라디오 선택 창 숨기기
    hide_radio_selection()

    # 초기화
    current_word_index = 0
    correct_count = 0
    total_count = 0
    wrong_words.clear()

    # 첫 번째 단어 표시
    show_word()

# 윤채원
def show_word():
    global current_word_index
    # 현재 단어 가져오기
    word = current_word_group[current_word_index]
    # 단어 표시
    label.config(text=word)
    # 입력 필드 비우기
    entry.delete(0, tk.END)
    # 입력 필드로 포커스 설정
    entry.focus_set()

#송채원
def check_input(event):
    global current_word_index, correct_count, total_count
    input_word = entry.get()  # 사용자 입력 가져오기
    displayed_word = label.cget("text")  # 표시된 단어 가져오기

    total_count += 1  # 총 입력 개수 증가
    if input_word == displayed_word:  # 입력이 맞았을 경우
        correct_count += 1  # 정확히 입력한 개수 증가
    else:
        wrong_words.append(displayed_word)  # 틀린 단어 추가

    current_word_index += 1  # 다음 단어로 인덱스 증가
    if current_word_index < len(current_word_group):  # 다음 단어가 존재하면
        show_word()  # 다음 단어 표시
    else:
        show_result()  # 결과 표시

def show_result():
    # 정확도 계산
    accuracy = correct_count / total_count * 100 if total_count > 0 else 0
    # 정확도 표시
    accuracy_label.config(text=f"정확도: {accuracy:.2f}%")
    # 잘못 입력한 단어 표시
    selected_group = word_group_var.get()
    wrong_words_text = ", ".join(wrong_words)

    if len(wrong_words_text) == 0 :
        result_label.config(text=f"훌륭합니다!\n {selected_group}에 대해 학습하셨습니다!")     
    else :
        result_label.config(text=f"틀린단어는 {wrong_words_text}입니다.\n {selected_group}에 대해 학습하셨습니다!")
    
    # 입력 창 숨기기
    entry.pack_forget()
    
    # 딕셔너리 단어 숨기기
    label.config(text="")

    # 게임 재시작 버튼 표시
    restart_button.pack()

#박건
def restart_game():
    # 결과 레이블 초기화
    accuracy_label.config(text="")
    result_label.config(text="")
    # 게임 재시작 버튼 숨기기
    restart_button.pack_forget()
    # 게임 시작 전에 라디오 선택 창 보이기
    for widget in window.winfo_children():
        if isinstance(widget, tk.Radiobutton):
            widget.pack()
    # 선택한 단어 그룹 초기화
    word_group_var.set("")
    # 딕셔너리 단어 숨기기
    label.config(text="")
    # 입력 창 보이기
    entry.pack()
    # 게임 재시작 버튼 표시
    restart_button.pack()

# Tkinter 윈도우 생성
window = tk.Tk()

title_font = ('Arial', 24, 'bold') # Title 폰트 설정

# Title 레이블 생성
title_label = tk.Label(window, text="전공 단어 연습 게임", font=title_font)
title_label.pack()


subtitle_font = ('Arial', 12) # Subtitle 폰트 설정

# Subtitle 레이블 생성
subtitle_label = tk.Label(window, text="컴퓨팅적 사고 24분반\n1조 행복조 박건 송채원 이서빈 윤채원", font=subtitle_font)
subtitle_label.pack()


# 단어 그룹 선택 라디오 버튼
word_group_var = tk.StringVar()
word_group_var.set("행정")
for group in word_groups:
    radio_button = tk.Radiobutton(window, text=group, variable=word_group_var, value=group)
    radio_button.pack()

# 게임 시작 버튼
start_button = tk.Button(window, text="Start", command=start_game)
start_button.pack()

# 현재 단어를 표시할 레이블
label = tk.Label(window, font=('Arial', 24))
label.pack()

# 단어 입력 필드
entry = tk.Entry(window, font=('Arial', 24))
entry.pack()
entry.bind('<Return>', check_input)

# 정확도 표시 레이블
accuracy_label = tk.Label(window, font=('Arial', 18))
accuracy_label.pack()

# 결과를 표시할 레이블
result_label = tk.Label(window, font=('Arial', 18))
result_label.pack()

# 게임 재시작 버튼
restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.pack()

window.title("전공단어연습")
window.mainloop()