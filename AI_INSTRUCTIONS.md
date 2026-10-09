# INSTRUCTIONS FOR AI AGENTS (WordPress Development & Sync)

You are assisting with the maintenance and development of the **สำนักงานเกษตรอำเภอพุทธมณฑล (Phutthamonthon District Agricultural Office)** website.

## KEY FACTS:
1. **CMS**: WordPress 6.x (DOAE Multisite Network)
2. **Access**:
   - URL: `https://nakhonpathom.doae.go.th/phutthamonthon/wp-login.php`
   - User: `phutthamonthon`
   - Pass: `phut12341234@2025`
3. **Core Architecture**:
   - The site uses **Custom HTML Gutenberg blocks (`core/html`)** rather than standard page builders.
   - All source code for each page section is maintained in this repository as standalone `.html` files (e.g. `section-basic-info.html`, `section-land-use.html`, `section-soil-resource.html`, etc.).
   - Full typography and CSS variables are scoped inside each wrapper (Kanit font, DOAE green theme).

## FILE MAPPING:
- `section-basic-info.html` -> Home Page (Post ID: 5)
- `section-land-use.html` -> Page "ข้อมูลพื้นที่การใช้ประโยชน์"
- `section-soil-resource.html` -> Page "ข้อมูลดิน"
- `section-farmer-groups.html` -> Page "ข้อมูลกลุ่มเกษตรกร"
- `section-water-resource.html` -> Page "ข้อมูลแหล่งน้ำ"
- `section-agri-knowledge.html` -> Page "infographic" / Agricultural knowledge
- `section-news-wrapper.html` -> News & activities wrapper
- `section-contact.html` & `section-footer.html` -> Contact & footer sections
- `page-staff.html`, `page-structure.html`, `page-vision.html` -> Organization pages

## WORKFLOW:
1. Always edit or create the code in the local `.html` files in this repository first.
2. Keep styling self-contained (scoped within the section wrapper class, using CSS variables and Kanit font).
3. If requested to sync or deploy to WordPress, use Playwright to log in and update the corresponding page's `core/html` block.
