import cv2

def check_available_cameras(min_index=0, max_index=10):
    print(f"\n[SCAN] Checking cameras from index {min_index} to {max_index}...\n")

    available = []

    for idx in range(min_index, max_index + 1):
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            print(f"  >> Camera detected at index {idx}")
            available.append(idx)
            cap.release()
        else:
            print(f"     No camera at index {idx}")

    if available:
        print("\n[RESULT] Available camera indices:", available)
    else:
        print("\n[RESULT] No active cameras found on this system.")

    return available


def main():
    # 기본은 0~10, 필요하면 함수 인자로 조절
    check_available_cameras(0, 10)


if __name__ == "__main__":
    main()