# Kịch bản thuyết trình PA2 — 20 phút / 5 người

**Nhóm:** 06  
**Chủ đề:** Freestyle Chess mobile website trên trình duyệt smartphone  
**Mục tiêu trình bày:** Không đọc lại toàn bộ báo cáo; chỉ kể mạch chính theo yêu cầu PA2: nghiên cứu người dùng → phân tích vấn đề → proposal → use case/flow cho từng solution.

---

## 1. Phân bổ thời gian tổng thể

| Phần | Người nói | Thời lượng | Mục tiêu |
|---|---:|---:|---|
| Mở đầu, scope, research setup | Người 1 | 3:00 | Cho giảng viên hiểu nhóm nghiên cứu ai, bằng cách nào, trong bối cảnh nào |
| Findings và chọn vấn đề | Người 2 | 4:00 | Chứng minh vấn đề được chọn có dữ liệu, không phải cảm tính |
| Problem 1 + Solution CS1.1 + UC-01 | Người 3 | 4:00 | Trình bày navigation trong thumb zone |
| Problem 1 + Solution CS1.2 + UC-02 | Người 4 | 3:30 | Trình bày FAB cá nhân hóa vị trí |
| Problem 2 + Solutions CS2.1/CS2.2 + UC-03/UC-04 + kết | Người 5 | 5:30 | Trình bày search/filter và kết luận theo requirement |
| **Tổng** | **5 người** | **20:00** |  |

> Gợi ý: Nếu phải rút xuống 10 phút, giữ Người 1 = 1 phút, Người 2 = 2 phút, mỗi solution = 1.5 phút, kết = 30 giây.

---

## 2. Slide outline đề xuất

| Slide | Nội dung | Người nói | Thời lượng |
|---:|---|---:|---:|
| 1 | Title + product scope | 1 | 0:30 |
| 2 | Research methods: survey + interview | 1 | 1:45 |
| 3 | User profile & mobile context | 1 | 0:45 |
| 4 | Key findings | 2 | 1:30 |
| 5 | Affinity clusters | 2 | 1:00 |
| 6 | Priority matrix & selected problems | 2 | 1:30 |
| 7 | Overall concept & design principles | 3 | 0:45 |
| 8 | P-01 + CS1.1 Bottom Navigation | 3 | 1:45 |
| 9 | UC-01 diagram/flow after CS1.1 | 3 | 1:30 |
| 10 | CS1.2 Draggable FAB | 4 | 1:45 |
| 11 | UC-02 diagram/flow after CS1.2 | 4 | 1:30 |
| 12 | P-02 + CS2.1 Sticky Search | 5 | 1:30 |
| 13 | UC-03 diagram/flow after CS2.1 | 5 | 1:00 |
| 14 | CS2.2 Faceted Filter Chips | 5 | 1:30 |
| 15 | UC-04 diagram/flow after CS2.2 | 5 | 1:00 |
| 16 | Trade-off summary + closing | 5 | 0:30 |

---

## 3. Kịch bản nói chi tiết

### Người 1 — Mở đầu, scope, research setup (3 phút)

**Slide 1 — Title + product scope (0:30)**

“Chào thầy/cô và các bạn. Nhóm 06 trình bày PA2 cho sản phẩm Freestyle Chess mobile website. Scope của nhóm là trải nghiệm trên smartphone browser, không phải native app. Vì vậy, toàn bộ nghiên cứu và proposal đều tập trung vào bối cảnh người dùng cầm điện thoại, xem nhanh thông tin giải đấu, rating, tin tức và video.”

**Slide 2 — Research methods (1:45)**

“Nhóm dùng hai phương pháp chính. Thứ nhất là online survey với 72 responses. Người tham gia được yêu cầu mở website Freestyle Chess bằng smartphone, khám phá khoảng 3 đến 5 phút, rồi trả lời các câu hỏi về homepage, navigation, rating, news, schedule, video và bối cảnh sử dụng mobile.

Thứ hai là direct interview/observation với 13 phiên. Ở phần này, nhóm không ép người dùng đi theo một kịch bản quá cứng, mà dùng semi-structured tasks: xem ấn tượng trang chủ, thử điều hướng, tìm thông tin player/rating, tìm tin tức giải đấu, dùng video/livestream và thử thao tác một tay. Mục tiêu là quan sát các khoảnh khắc người dùng bị chậm, lúng túng, đổi cách cầm điện thoại hoặc nói ra frustration.

Điểm nhóm muốn nhấn mạnh là survey cho bức tranh rộng, còn interview giúp nhìn thấy hành vi thật: người dùng có với ngón tay không, có đổi grip không, có scroll quá lâu không, và search fail ở đâu.”

**Slide 3 — User profile & mobile context (0:45)**

“Một vài con số quan trọng: 63.9% người dùng thường dùng smartphone để đọc tin thể thao hoặc cờ vua. 44.4% thường cầm điện thoại một tay, và 41.7% thay đổi cách cầm tùy tình huống. Ngoài ra, 52.8% chưa từng nghe đến Freestyle Chess trước khảo sát, nên website không chỉ phục vụ fan cứng mà còn phải hỗ trợ người mới. Vì vậy, nhóm ưu tiên các vấn đề xảy ra trong phiên dùng ngắn, trên màn hình nhỏ, và khi người dùng không có nhiều kiên nhẫn để thử đi thử lại.”

**Chuyển ý sang Người 2:**  
“Từ setup đó, phần tiếp theo sẽ nói ngắn gọn: nhóm tìm thấy gì, và vì sao chỉ chọn một vài vấn đề để giải quyết.”

---

### Người 2 — Findings và chọn vấn đề (4 phút)

**Slide 4 — Key findings (1:30)**

“Từ survey và interview, nhóm rút ra năm insight chính, nhưng trong bài thuyết trình chỉ cần nhấn mạnh ba insight ảnh hưởng trực tiếp đến proposal.

Thứ nhất, người dùng mobile muốn truy cập nhanh thông tin chính: match results, latest news, rating và player information. Đây là các nội dung phù hợp với phiên sử dụng ngắn khoảng 2 đến 3 phút.

Thứ hai, navigation hiện tại không phải là không nhìn thấy. Điểm dễ tìm menu là 3.94/5. Vấn đề nằm ở reachability: menu hamburger nằm top-left, trong khi nhiều người cầm máy một tay. 43.1% báo cáo phải với ngón tay, đổi grip hoặc dùng tay còn lại.

Thứ ba, việc tìm thông tin trên list dài chưa đủ tốt. 61.1% gặp khó khăn khi không nhớ chính xác tên player, event hoặc thông tin cần tìm. Với list dài như Rating và News, người dùng muốn filter, sticky search, pagination hoặc suggestion hơn là chỉ scroll.”

**Slide 5 — Affinity clusters (1:00)**

“Ở Requirement 2, nhóm đưa các quan sát và ý tưởng lên affinity diagram. Các sticky notes được gom thành bốn cluster: Ergonomic Navigation, Homepage Onboarding, Search & Information Retrieval, và Video Player Interaction.

Điểm quan trọng ở đây là nhóm không nhảy thẳng từ ‘tôi nghĩ vậy’ sang solution. Mỗi cluster đều có evidence từ survey hoặc interview. Ví dụ, cluster navigation có các note về top-left hamburger gây khó thao tác một tay; cluster search có các note về rating list, news list và việc search fail khi nhập không đúng thứ tự tên.”

**Slide 6 — Priority matrix & selected problems (1:30)**

“Sau affinity diagram, nhóm dùng priority matrix với bốn tiêu chí: frequency, severity, evidence strength và feasibility. Kết quả có bốn vấn đề nổi bật: P-01 navigation reachability đạt 19/20; P-02 search/filtering trên list dài đạt 18/20; P-03 video feedback/audio overlap cũng 18/20; P-04 homepage onboarding đạt 16/20.

Nhóm chọn tập trung vào P-01 và P-02 cho proposal. Lý do là đề yêu cầu không cần giải quyết nhiều vấn đề, mà nên chọn một vài tough problems. P-01 và P-02 vừa có điểm ưu tiên cao, vừa là vấn đề UX interaction-model rõ ràng. P-03 được ghi nhận, nhưng nhóm xem nó thiên về bug hoặc implementation fix như loading feedback và single-player logic hơn là một hướng conceptual redesign chính. P-04 quan trọng với người mới, nhưng severity thấp hơn và không phải trọng tâm của Requirement 3 trong proposal hiện tại.”

**Chuyển ý sang Người 3:**  
“Từ hai vấn đề được chọn, nhóm giữ sản phẩm là responsive mobile website, nhưng thay đổi interaction model. Phần sau là Problem 1: thao tác navigation một tay.”

---

### Người 3 — Problem 1, CS1.1 và UC-01 (4 phút)

**Slide 7 — Overall concept & design principles (0:45)**

“Overall concept của nhóm là không chuyển sang app mới, mà redesign mobile website hiện tại theo ba nguyên tắc. Một là thumb-zone-first: control quan trọng nên nằm trong vùng với tự nhiên của ngón cái. Hai là zero-step hoặc one-step access: thao tác chính không nên bị giấu sau nhiều bước. Ba là flexible input: nếu bắt người dùng nhớ chính xác tên hoặc thứ tự, interface cần hỗ trợ nhập gần đúng hoặc thay bằng lựa chọn tap.”

**Slide 8 — P-01 + CS1.1 Bottom Navigation (1:45)**

“Vấn đề P-01 là hamburger menu nằm top-left. Người dùng có thể thấy nó, nhưng khi cầm máy một tay, nhất là tay phải, họ phải với ngón cái lên góc trái, đổi grip hoặc dùng tay còn lại. Đây là vấn đề vật lý của mobile interaction, không chỉ là vấn đề layout.

Solution đầu tiên là CS1.1: Persistent Bottom Navigation Bar. Ý tưởng là đưa các destination chính xuống dưới cùng màn hình, cố định trong viewport. Các tab chính gồm Home, News, Schedule, Rating, Videos & Streams. Vì menu gốc của site có nhiều hơn năm mục, nhóm thêm mục More để chứa Press & Media, Rules & FC Players Club, Merch và Masterclass.

Điểm mạnh của solution này là rất quen thuộc với người dùng mobile, luôn visible, ít rủi ro discoverability, và task chuyển trang chỉ còn một tap. Trade-off là nó chiếm một phần chiều cao màn hình và không scale tốt nếu sau này site có quá nhiều mục top-level.”

**Slide 9 — UC-01 diagram/flow after CS1.1 (1:30)**

“Sau solution CS1.1 là use case tương ứng UC-01: Navigate via Persistent Bottom Navigation Bar.

Actor chính là Mobile Visitor, artifact chính là Bottom Navigation Bar và Main View Container. Flow thành công rất ngắn: người dùng đang ở bất kỳ trang nào, nhìn thấy bottom nav cố định ở phần dưới màn hình, tap vào tab như Rating, hệ thống highlight active tab, hiển thị loading feedback nếu cần, rồi render Rating page.

Alternative flow là nếu người dùng tap lại tab đang active, hệ thống scroll về đầu trang thay vì không phản hồi. Exception flow là nếu mạng chậm, hệ thống giữ bottom nav active và hiển thị skeleton loader hoặc retry. Như vậy use case này trực tiếp giải quyết mục tiêu: zero grip adjustment và one-tap navigation.”

**Chuyển ý sang Người 4:**  
“Tuy nhiên, bottom nav là layout cố định cho tất cả mọi người. Solution thứ hai thử một hướng cá nhân hóa hơn.”

---

### Người 4 — CS1.2 và UC-02 (3 phút 30 giây)

**Slide 10 — CS1.2 Draggable FAB (1:45)**

“Solution thứ hai cho P-01 là CS1.2: Draggable Floating Action Button. Thay vì một bar cố định, website có một nút tròn nổi, mặc định nằm dưới bên phải. Người dùng có thể kéo nút này đến vị trí thuận tay, ví dụ dưới bên trái nếu thuận tay trái hoặc đang cầm máy theo cách khác.

Khi tap vào FAB, nó mở navigation menu gồm các destination chính giống CS1.1 và thêm More cho các mục phụ. Interaction rules gồm: press-and-hold để drag, release thì snap vào cạnh gần nhất, lưu vị trí cho lần truy cập sau bằng local storage, và movement dưới khoảng 5px thì tính là tap chứ không phải drag.

Điểm mạnh là nó thích nghi với handedness và bối cảnh cầm máy, đồng thời ít chiếm diện tích khi idle. Điểm yếu là discoverability thấp hơn bottom nav, vì không phải ai cũng biết nút có thể kéo; menu mở ra cũng có thể che nội dung bên dưới.”

**Slide 11 — UC-02 diagram/flow after CS1.2 (1:30)**

“Use case tương ứng là UC-02: Access Navigation Menu via Draggable FAB.

Actor vẫn là Mobile Visitor, nhưng artifact chính là Draggable FAB và Floating Navigation Drawer. Flow thành công gồm hai pha. Pha đầu là personalization: người dùng nhấn giữ và kéo FAB đến vùng ngón cái dễ chạm, hệ thống hiển thị feedback bằng shadow hoặc trạng thái drag, rồi snap và lưu vị trí. Pha hai là navigation: người dùng tap FAB, menu mở ra, chọn Schedule hoặc News, hệ thống chuyển trang và collapse FAB.

Exception flow là accidental drag: nếu khoảng di chuyển quá nhỏ, hệ thống hiểu đó là tap để mở menu. Điểm quan trọng của UC-02 là nó không giả định một thumb zone cố định cho tất cả user, mà để user tự đặt control vào vùng thoải mái của họ.”

**Chuyển ý sang Người 5:**  
“Sau navigation, vấn đề lớn thứ hai là tìm thông tin trong các list dài như Rating và News.”

---

### Người 5 — Problem 2, CS2.1/CS2.2, UC-03/UC-04 và kết luận (5 phút 30 giây)

**Slide 12 — P-02 + CS2.1 Sticky Search (1:30)**

“Problem 2 là lack of sticky search and filtering. Rating leaderboard và News feed là các list dài, nhưng người dùng thường chỉ có vài phút để tìm thông tin. 61.1% gặp khó khăn khi không nhớ chính xác tên player hoặc event. Interview cũng cho thấy search hiện tại dễ fail nếu người dùng nhập tên theo thứ tự tự nhiên, ví dụ ‘Liem Le’ thay vì format hệ thống đang lưu.

CS2.1 là Sticky Search Bar with Flexible Name Matching. Search bar cố định ở đầu viewport trên Rating và News, có nút clear và live auto-suggest. Phần quan trọng không chỉ là sticky UI, mà là matching logic: hệ thống tokenize query, không phụ thuộc thứ tự first name/last name, và nên diacritic-insensitive. Ví dụ ‘Liem’, ‘Liem Le’ hoặc ‘Le Liem’ đều có thể dẫn tới Le Quang Liem.

Trade-off: solution này rất tốt cho người đã biết tên hoặc nhớ một phần tên, nhưng vẫn chưa đủ cho người chỉ biết thuộc tính như title GM/FM hoặc rating range.”

**Slide 13 — UC-03 diagram/flow after CS2.1 (1:00)**

“Use case UC-03 là Search Player Rating via Flexible Sticky Search Bar.

Actor chính là Chess Follower hoặc Mobile Visitor. Flow: người dùng vào Rating page, scroll xuống nhưng search bar vẫn sticky, tap vào field, nhập partial name theo bất kỳ thứ tự nào, hệ thống chạy flexible matching và hiện auto-suggest, người dùng chọn result, hệ thống highlight hoặc scroll đến player row. Nếu không có kết quả, hệ thống hiển thị no-match state kèm suggestion thay vì để list trống im lặng. Use case này nhắm vào mục tiêu tìm player trong 3 đến 5 giây, không phải scroll thủ công.”

**Slide 14 — CS2.2 Faceted Filter Chips (1:30)**

“Vì CS2.1 vẫn phụ thuộc vào việc gõ, nhóm đề xuất solution khác biệt hơn là CS2.2: Faceted Filter Chips. Thay vì bắt user nhớ và nhập tên, interface đưa ra các chiều lọc mà người dùng thật sự quan tâm: title như GM, IM, FM; rating range như Rating > 2700; hoặc event/date trên News page.

Các chip nằm ngay dưới page title, có thể scroll ngang. Khi tap vào chip, list cập nhật ngay, không cần confirm và không cần mở keyboard. Nhiều chip có thể active cùng lúc theo logic AND, ví dụ GM và Rating > 2700. Nếu không có kết quả, hệ thống hiển thị empty state rõ ràng với nút Reset Filters.

Điểm mạnh là rất phù hợp với người mới hoặc casual user: họ có thể không nhớ tên player, nhưng biết họ muốn xem grandmaster hoặc sự kiện gần đây. Điểm yếu là nếu user đã biết chính xác tên cần tìm, filter chips có thể chậm hơn search trực tiếp.”

**Slide 15 — UC-04 diagram/flow after CS2.2 (1:00)**

“Use case UC-04 là Filter Content via Faceted Filter Chips.

Actor chính là First-Time Visitor hoặc Event-Driven Viewer. Flow: người dùng vào Rating hoặc News, nhìn thấy hàng filter chips, tap GM, hệ thống đổi chip sang active state và update list. Người dùng tap thêm Rating > 2700, hệ thống combine filter và hiển thị list đã thu hẹp. Alternative flow là tap lại chip để bỏ chọn. Exception flow là empty result thì hiện message và Reset Filters. Use case này giải quyết nhu cầu zero-typing filtering.”

**Slide 16 — Trade-off summary + closing (0:30)**

“Tóm lại, PA2 của nhóm đi từ dữ liệu đến quyết định thiết kế. Research cho thấy hai vấn đề UX quan trọng nhất là navigation reachability và information retrieval. Với mỗi vấn đề, nhóm không đưa một answer duy nhất mà đề xuất hai conceptual solutions khác nhau: bottom nav so với draggable FAB, sticky flexible search so với filter chips. Sau mỗi solution, use case/flow chỉ rõ actor, artifact và interaction. Đây sẽ là nền tảng để nhóm bước sang prototype và evaluation ở các phase tiếp theo. Cảm ơn thầy/cô và các bạn.”

---

## 4. Những phần nên bỏ qua hoặc chỉ nói rất nhanh

- Không đọc toàn bộ 29 câu hỏi survey; chỉ nói survey có 72 responses và bao phủ homepage, navigation, search, video.
- Không đọc từng participant interview; chỉ dùng ví dụ P01/P02/P03 cho navigation và P06/P09/P10 cho search.
- Không trình bày chi tiết toàn bộ sticky notes; chỉ nói có bốn affinity clusters.
- Không dành nhiều thời gian cho P-03 video và P-04 onboarding; chỉ nói vì sao chưa chọn làm proposal chính.
- Không đọc use case specification dạng bảng đầy đủ; chỉ nói actor, artifact, main flow, alternative/exception nổi bật.

---

## 5. Gợi ý Q&A nhanh

**Hỏi:** Vì sao P-03 cũng 18/20 nhưng không chọn?  
**Trả lời:** P-03 quan trọng, nhưng phần lớn là media playback behavior như auto-pause video cũ, loading spinner, button state. Nhóm xem đây là bug/implementation fix rõ hơn là một hướng conceptual UX solution chính. P-01 và P-02 tác động trực tiếp đến interaction model của mobile website.

**Hỏi:** Vì sao search bar vẫn ở trên cùng, không hoàn toàn theo thumb-zone-first?  
**Trả lời:** Nhóm chấp nhận trade-off. Vấn đề cũ là một icon nhỏ ở góc top-left cần với chính xác; sticky search full-width có target rộng hơn và luôn visible khi scroll. Với người không muốn gõ, CS2.2 filter chips là hướng zero-typing thay thế.

**Hỏi:** Bottom nav có quá nhiều mục không?  
**Trả lời:** Có, nên nhóm chỉ giữ 5 core destinations: Home, News, Schedule, Rating, Videos & Streams. Các mục còn lại nằm trong More bottom-sheet.

**Hỏi:** FAB có thể che nội dung không?  
**Trả lời:** Có, đây là trade-off chính. Vì vậy FAB phù hợp như một conceptual alternative cho nhóm user cần cá nhân hóa reachability, còn bottom nav an toàn hơn về discoverability.

**Hỏi:** Có cần native app không?  
**Trả lời:** Không. Scope PA1/PA2 của nhóm là mobile website trên smartphone browser. Proposal giữ nguyên platform, chỉ thay đổi interaction model.
