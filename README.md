# NewEra-Cash-Carry
Mana, yuqoridagi README.md faylini to'liq Markdown formatida quyidagicha yozib berdim:

markdown
Copy
Edit
# Store Management System

Bu loyiha do'konni boshqarish tizimi uchun yaratilgan Python dasturidir. Ushbu tizimda foydalanuvchilar turli rollarga ega: mijoz, admin va superadmin. Har bir rol o'ziga xos funktsiyalar va imkoniyatlarga ega bo'lib, tizim orqali foydalanuvchilar ma'lumotlarini boshqarish mumkin.

## Asosiy imkoniyatlar
- **Mijozlar** tizimga kirib, o'z profilingizni ko'rish va yangilash imkoniyatiga ega bo'lishadi.
- **Admin** foydalanuvchilarga boshqaruv ruxsatlarini beradi, mahsulotlarni va buyurtmalarni boshqaradi.
- **Superadmin** yuqori darajadagi boshqaruv ruxsatlariga ega bo'lib, tizimning barcha funksiyalarini boshqaradi.

2. Ma'lumotlar bazasini tayyorlash:
Dasturda ma'lumotlarni saqlash uchun SQLite ma'lumotlar bazasidan foydalaniladi. Dastur ishga tushirilganda, store.db nomli ma'lumotlar bazasi yaratiladi va foydalanuvchi ma'lumotlari saqlanadi.

3. Virtual Muhit:
Agar siz virtual muhitdan foydalanishni xohlasangiz, quyidagicha virtual muhit yaratib, faollashtiring:

Virtual muhit yaratish:

bash
python -m venv venv
Virtual muhitni faollashtirish:

Mac/Linux:
bash
source venv/bin/activate
Windows:
bash
.\venv\Scripts\activate
Foydalanish
Dasturga kirish:

Dastur ishga tushirilganda foydalanuvchi loginini kiritadi.
Agar foydalanuvchi tizimda mavjud bo'lsa, parolni kiritish talab qilinadi.
Agar foydalanuvchi yangi bo'lsa, tizim yangi foydalanuvchi yaratish uchun imkoniyat beradi.
Foydalanuvchining roli:

Tizim foydalanuvchining rolini aniqlaydi: mijoz, admin yoki superadmin.
Tegishli rolga qarab, foydalanuvchiga mos menyu ko'rsatiladi.
Mijozlar o'z profilingizni ko'rish va yangilash imkoniyatiga ega.

Adminlar foydalanuvchilarni boshqarish va mahsulotlar bilan ishlash imkoniyatiga ega.

Superadminlar tizimning barcha funksiyalarini boshqaradi va yuqori darajadagi ruxsatlarni belgilaydi.

Tizimda ishlash
Tizimda ro'yxatdan o'tgan foydalanuvchilarning ma'lumotlari store.db SQLite ma'lumotlar bazasida saqlanadi.

Mualliflar
Muhammadjon Merzaqulov
Litsenziya
Bu loyiha MIT Litsenziyasi asosida litsenziyalangan.
