def main():
    questions = [
        (
            "你早晨起床後通常做什麼？",
            ["靜坐冥想或感恩", "查看手機訊息", "直接投入工作或學習", "賴床繼續睡"],
            [3, 1, 2, 0],
        ),
        (
            "當你感到心煩意亂時，你會？",
            ["深呼吸或冥想", "找朋友訴苦", "看書或影片轉移注意", "壓抑情緒假裝沒事"],
            [3, 1, 2, 0],
        ),
        (
            "在人際相處中，你最重視？",
            ["心靈連結與同理", "價值觀是否相近", "彼此能否獲益", "只要不打擾我都好"],
            [3, 2, 1, 0],
        ),
        (
            "你是否有固定的靈性練習？",
            ["每天都有", "偶爾想到才做", "很少甚至沒有", "完全沒有"],
            [3, 2, 1, 0],
        ),
        (
            "你如何看待生活中的困難？",
            ["是自我成長的契機", "必要的磨練，雖然會抱怨", "只想快點逃避", "為什麼偏偏是我？"],
            [3, 2, 1, 0],
        ),
    ]

    total_score = 0
    for idx, (question, options, scores) in enumerate(questions, start=1):
        print(f"\n問題 {idx}: {question}")
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")

        while True:
            choice = input("請輸入你的選擇 (1-4)：")
            if choice in {"1", "2", "3", "4"}:
                total_score += scores[int(choice) - 1]
                break
            print("輸入錯誤，請輸入 1-4。")

    # 判定等級
    if total_score >= 13:
        level = "宗師級"
        comment = "恭喜！你已達到宗師級，快把你的智慧分享給大家吧！"
    elif total_score >= 9:
        level = "高階"
        comment = "你的靈性已相當強大，繼續保持！"
    elif total_score >= 5:
        level = "中階"
        comment = "不錯喔，再持續努力，靈性會更提升！"
    else:
        level = "初階"
        comment = "多加練習，相信你能發現更多內在力量！"

    print("\n==== 測驗完成 ====")
    print(f"你的靈性開發程度：{level}")
    print(comment)


if __name__ == "__main__":
    main()
