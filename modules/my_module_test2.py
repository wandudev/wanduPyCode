def func(a):
    print("입력 숫자:", a)
    
if __name__ == "__main__":
    print("모듈을 직접 실행할 때만 실행되는 코드")
    func(3)
    func(4)
else:
    print("모듈을 임포트해서 실행")
        
    
