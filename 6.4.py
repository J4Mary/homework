def dom(n,e,k):
    pod=(n-1)//(e*k)+1
    et=(n-(pod-1)*e*k)//k
    print("Подъезд", pod, "этаж", et)
dom(15,5,3)