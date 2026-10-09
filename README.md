# คู่มือการทำงานและสถาปัตยกรรมเว็บไซต์ (AI & Developer Guide)
**สำนักงานเกษตรอำเภอพุทธมณฑล จังหวัดนครปฐม**  
*(กรมส่งเสริมการเกษตร - DOAE)*

---

> ### 🔐 ข้อมูลเข้าสู่ระบบ WordPress (Login Credentials)
> - **Login URL**: `https://nakhonpathom.doae.go.th/phutthamonthon/wp-login.php`
> - **Username**: `phutthamonthon`
> - **Password**: `phut12341234@2025`
> - **Front-end**: `https://nakhonpathom.doae.go.th/phutthamonthon/`
> - **Admin URL**: `https://nakhonpathom.doae.go.th/phutthamonthon/wp-admin/`

---

## 📌 1. ข้อมูลระบบและการเข้าถึง (System Overview)

- **Production URL**: `https://nakhonpathom.doae.go.th/phutthamonthon/`
- **WP Admin Login**: `https://nakhonpathom.doae.go.th/phutthamonthon/wp-login.php`
- **Username**: `phutthamonthon`
- **Password**: `phut12341234@2025`
- **CMS Environment**: WordPress 6.9 (เครือข่าย DOAE Multisite)
- **Active Theme**: Astra
- **Plugins สำคัญที่ใช้งาน**: Gutentor, Smart Slider 3, EmbedPress, FileBird, Shortcoder

---

## 🏗️ 2. สถาปัตยกรรมเว็บไซต์ (Core Architecture)

โปรเจกต์นี้ไม่ได้ใช้ Page Builder แบบลากวาง (เช่น Elementor) ในการจัดหน้า แต่ใช้แนวทาง:
> **"Modular HTML/CSS Components -> Gutenberg Custom HTML Block (`<!-- wp:html -->`)"**

### เหตุผลและหลักการออกแบบ:
1. **เลี่ยงข้อจำกัดของระบบ Multisite ราชการ**: ลดปัญหา plugin conflict หรือสิทธิ์การติดตั้ง plugin เสริม
2. **ควบคุม UI/UX ได้ 100%**: ปรับแต่ง CSS Flexbox, Grid, Gradient, Hover effects และ Micro-animations ได้อิสระ
3. **CSS-Only & Lightweight**: หลีกเลี่ยง JavaScript ที่ซับซ้อนเพื่อไม่ให้ถูกบล็อกโดย CSP/Security ของหน่วยงานราชการ
4. **Custom Font**: ใช้ Google Fonts (`Kanit`) เป็นฟอนต์หลักในการสื่อสาร

---

## 🗺️ 3. แผนผังการจับคู่ไฟล์ในโปรเจกต์กับหน้า WordPress (File Mapping)

| ไฟล์ใน Workspace | ปลายทางใน WordPress | หมายเหตุ / ส่วนที่แสดงผล |
| :--- | :--- | :--- |
| `section-basic-info.html` | **หน้าแรก (Home)** [Post ID: 5] | ข้อมูลพื้นฐานสำนักงาน, บัตรข้อมูลสรุป, แผนที่ |
| `section-land-use.html` | **หน้า "ข้อมูลพื้นที่การใช้ประโยชน์"** | สถิติและรายละเอียดการใช้ที่ดินทางการเกษตร |
| `section-soil-resource.html` | **หน้า "ข้อมูลดิน"** | ข้อมูลชุดดิน ลักษณะดิน ปัญหาดิน และแนวทางแก้ไข |
| `section-farmer-groups.html` | **หน้า "ข้อมูลกลุ่มเกษตรกร"** | วิสาหกิจชุมชน, แปลงใหญ่, กลุ่มแม่บ้านเกษตรกร |
| `section-water-resource.html` | **หน้า "ข้อมูลแหล่งน้ำ"** | ระบบชลประทาน คลอง แหล่งน้ำเพื่อการเกษตร |
| `section-agri-knowledge.html` | **หน้า "infographic" / คลังความรู้** | สื่อความรู้การเกษตร, หรือฝัง `https://kasetinfo.netlify.app/` |
| `section-news-wrapper.html` | **หน้าข่าวสาร / กิจกรรม** | กรอบแสดงข่าวกิจกรรมและประชาสัมพันธ์ |
| `section-contact.html` | **หน้าติดต่อเรา** | ช่องทางการติดต่อ แผนที่ ที่อยู่ |
| `section-footer.html` | **ส่วนท้ายเว็บ (Footer)** | ลิงก์หน่วยงานที่เกี่ยวข้อง ลิขสิทธิ์ |
| `page-staff.html` | **หน้า "ทำเนียบบุคลากร"** | รายชื่อและตำแหน่งเจ้าหน้าที่สำนักงาน |
| `page-structure.html` | **หน้า "โครงสร้างองค์กร"** | แผนผังสายการบังคับบัญชา |
| `page-vision.html` | **หน้า "วิสัยทัศน์ / พันธกิจ"** | ยุทธศาสตร์และเป้าหมายการส่งเสริมการเกษตร |
| `color-palette.css` | **โทนสีหลักขององค์กร** | ตัวแปรสีเขียวเกษตร (Forest, Sage, Amber, Earth) |

---

## 🎨 4. มาตรฐานการเขียนโค้ดสำหรับ AI (Coding Standards)

เมื่อ AI ต้องแก้ไข ปรับปรุง หรือสร้างหน้า/โมดูลใหม่ ให้ปฏิบัติตามมาตรฐานนี้อย่างเคร่งครัด:

1. **Scoped CSS ในตัว Wrapper เสมอ**:
   - ต้องครอบโมดูลด้วย Container เฉพาะ เช่น `.basic-info-wrapper`, `.land-use-container`
   - ประกาศตัวแปรสีและค่าคงที่ภายในคลาสครอบ เพื่อไม่ให้กระทบธีมหลัก Astra:
     ```css
     .custom-module-wrapper {
         --primary-green: #1f6541;
         --primary-forest: #12452d;
         --accent-amber: #c87835;
         --bg-paper: #f5f7f0;
         font-family: 'Kanit', sans-serif;
     }
     ```
2. **Typography**:
   - ใส่ลิงก์นำเข้าฟอนต์ Kanit ไว้ด้านบนของไฟล์เสมอ:
     ```html
     <link rel="preconnect" href="https://fonts.googleapis.com">
     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
     <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
     ```
3. **Responsive Design (Mobile-First / Fluid)**:
   - ใช้ `clamp()` สำหรับ `font-size`, `padding`, `margin` เช่น `padding: clamp(20px, 4vw, 60px);`
   - ใช้ CSS Grid / Flexbox พร้อม `flex-wrap: wrap` รองรับทั้งมือถือ แท็บเล็ต และจอเดสก์ท็อป
4. **ความเข้ากันได้กับ WordPress (WordPress Compatibility)**:
   - ไม่เขียนแท็ก `<html>`, `<head>`, `<body>` ซ้ำซ้อนลงในหน้าย่อย (ยกเว้นหน้าที่ต้องการเป็น iframe หรือ standalone template)
   - ไฟล์ที่เป็น Section ย่อยควรเริ่มต้นด้วย `<style>...</style>` และ `<div>...</div>` ได้ทันที

---

## 🤖 5. เวิร์กโฟลว์การอัปเดตเว็บด้วย Playwright (Automation Sync Guide)

หากต้องการให้ AI อัปเดตเนื้อหาจากไฟล์ใน Workspace ขึ้นสู่ WordPress อัตโนมัติ:

1. **เข้าสู่ระบบ**:
   - เปิด URL: `https://nakhonpathom.doae.go.th/phutthamonthon/wp-login.php`
   - กรอก `#user_login` = `phutthamonthon`, `#user_pass` = `phut12341234@2025`
2. **แก้ไขหน้า (Edit Post/Page)**:
   - เข้าหน้า Editor: `https://nakhonpathom.doae.go.th/phutthamonthon/wp-admin/post.php?post={POST_ID}&action=edit`
   - บล็อกที่ใช้บรรจุโค้ดคือ Gutenberg Block ประเภท `core/html` (Custom HTML)
3. **อัปเดตโค้ด**:
   - สามารถอ่านไฟล์ `.html` จากเครื่อง แล้วนำ String ไปใส่ในบล็อก `core/html` หรือสั่งผ่าน Gutenberg JS API:
     ```javascript
     wp.data.dispatch('core/editor').editPost({ content: newHtmlContent });
     wp.data.dispatch('core/editor').savePost();
     ```
4. **ตรวจสอบความปลอดภัย**:
   - บันทึกการเปลี่ยนแปลงเฉพาะส่วนเนื้อหา ห้ามเปลี่ยนแปลงการตั้งค่า Core Settings หรือ Themes โดยไม่ได้รับคำสั่งจากผู้ใช้
