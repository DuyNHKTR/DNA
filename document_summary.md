# Tom tat tai lieu `document.pdf`

## Thong tin chung

- **Tieu de:** DNA Sequence Classification Using Machine Learning Models Based on k-mer Features
- **Tac gia:** Afthar Kautsar
- **Nguon:** Journal of Computers and Digital Business (JCBD), Vol. 4, No. 2, May 2025, trang 100-105
- **DOI:** https://doi.org/10.56427/jcbd.v4i2.762
- **Chu de:** Phan loai chuoi DNA/cfDNA bang dac trung `k-mer` va cac mo hinh hoc may

## Muc tieu nghien cuu

Tai lieu tap trung danh gia kha nang phan loai cac doan **cell-free DNA (cfDNA)** thanh nhom binh thuong va nhom dot bien/nguon goc khoi u bang cac mo hinh hoc may. Muc tieu chinh la kiem tra hieu qua cua bieu dien dac trung `k-mer` voi `k = 3` khi ap dung cho cac bo phan loai pho bien.

## Du lieu va phuong phap

- Chuoi DNA goc co do dai **126,033 base pairs**
- Dung phuong phap **k-mer** voi `k = 3`
- Sau phan manh tao ra **630 doan DNA**
- Moi doan duoc ma hoa thanh vector so theo **tan suat xuat hien cua 3-mer**
- Chia du lieu:
  - **80% train:** 504 mau
  - **20% test:** 126 mau
- Ba mo hinh duoc dem so sanh:
  - **Random Forest**
  - **Support Vector Machine (SVM)**
  - **Deep Neural Network (DNN)**

## Ket qua chinh

### 1. Do chinh xac tong the

- **Random Forest:** 71%
- **SVM:** 70%
- **DNN:** 67%

Theo phan ket qua va ket luan cua bai bao, **Random Forest la mo hinh co accuracy cao nhat**.

### 2. Hieu qua theo tung lop

Ca ba mo hinh deu nhan dien lop **mutation** tot hon ro ret so voi lop **normal**.

- **Random Forest**
  - `recall(normal) = 0.08`
  - `recall(mutation) = 0.99`
- **SVM**
  - `recall(normal) = 0.00`
  - `recall(mutation) = 1.00`
- **DNN**
  - `recall(normal) = 0.13`
  - `recall(mutation) = 0.91`

Dieu nay cho thay mo hinh bi lech manh ve phia lop dot bien.

## Dien giai ket qua

Tac gia cho rang nguyen nhan chinh khien cac mo hinh nhan dien kem lop `normal` la:

- **Mat can bang lop** trong tap du lieu kiem thu/training
- Dac trung `k-mer` don gian chua du de nam bat het do phuc tap cua chuoi binh thuong
- Kien truc va sieu tham so cua DNN chua duoc toi uu sau

Noi ngan gon, cach bieu dien du lieu hien tai du de bat cac mau dot bien ro rang, nhung chua du manh de tach tot cac mau binh thuong.

## Ket luan rut gon

- Cach tiep can dung `k-mer` ket hop ML/DL la **kha thi** cho bai toan phan loai cfDNA.
- Trong thi nghiem nay, **Random Forest cho ket qua tong the tot nhat**.
- Tuy vay, moi mo hinh deu gap van de lon o **lop normal**, nen ket qua chua du manh de xem la on dinh cho ung dung thuc te.
- Huong cai thien duoc de xuat:
  - can bang du lieu bang **SMOTE** hoac **ADASYN**
  - cai tien dac trung bang **embedding**
  - thu **attention** hoac **transformer-based models**

## Ghi chu quan trong

Co mot **diem khong nhat quan trong bai bao**:

- O phan **abstract**, tac gia viet rang **DNN dat hieu nang cao nhat**
- Nhung o phan **Results and Discussion** va **Conclusion**, so lieu lai cho thay **Random Forest dung dau voi accuracy 71%**

Vi vay, khi trich dan tai lieu nay, nen uu tien so lieu trong phan bang ket qua va dong thoi ghi chu rang bai bao co mau thuan noi dung giua abstract va phan thuc nghiem.

## Tom tat ngan

Bai bao nghien cuu phan loai cfDNA bang dac trung `3-mer` va ba mo hinh Random Forest, SVM, DNN. Ket qua thuc nghiem cho thay Random Forest dat accuracy cao nhat (71%), nhung ca ba mo hinh deu thien manh ve nhan dien chuoi dot bien va hoat dong kem voi chuoi binh thuong. Han che chinh nam o mat can bang du lieu va bieu dien dac trung con don gian; huong phat trien tiep theo la can bang du lieu tot hon va dung bieu dien/kien truc sau hon.
