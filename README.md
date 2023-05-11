# Algo
Try to code some algorithms
# 1. Bisection method  (áp dụng trong trường hợp pt chỉ có 1 nghiệm nằm trong khoảng phân ly cho trước)
Áp dụng đối với f(x) = $x^x-10$  
- Lưu đồ:  
![Diagram](https://github.com/huyvu15/Algo/blob/main/Bisection_Dia.png)  
Link Diagram: https://cacoo.com/diagrams/vp0zryKkYwpJ7JwO/B89E2  
- Result: 
![result_1](https://github.com/huyvu15/Algo/blob/main/Bisection.png)  

# 2. Iteration_method:
- Nhược điểm của phương pháp này là mình phải tìm hàm $\varphi$ thỏa mãn yêu cầu bài toán
- Sai số $10^{-7}$
Ta có:   
$x^3+x-1000=0$  
$\Leftrightarrow$ $x = \sqrt[3]{1000-x}$
- Đặt $\varphi (x)$ = $\sqrt[3]{1000-x}$

    $| \varphi ' (x) |$ = $\displaystyle|-\dfrac{1}{3}$ $\dfrac{1}{(\sqrt{1000-x})^3}|$ < $\dfrac{1}{3.990^{\frac{2}{3}}}$  < 1  
$\Rightarrow$ q = $\dfrac{1}{3.990^{\dfrac{2}{3}}}$  
$\Rightarrow$ Khi đó phương pháp lặp đơn hội tụ với pt đã cho $X_0 = 10 $, Xây dựng được dãy gần đúng theo công thức:  

    $X_{n+1}$ = $\sqrt[3]{1000-x}$
- Kết quả chạy thuật toán:  
![result_Iteration_method](https://github.com/huyvu15/Algo/blob/main/result_Iteration_method.png)  
Link Diagram: https://cacoo.com/diagrams/vp0zryKkYwpJ7JwO-16A4E.png 
