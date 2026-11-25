"""Tạo các file Word demo cho workshop (ngành y tế, đơn vị giả định).

File Chính sách Nhân sự được lưu dạng .docx tạm trong _gen/_pdf_src,
sau đó topdf.ps1 chuyển sang PDF bằng Word.
"""
from pathlib import Path

from docx_common import new_doc, title, para, bullets, table, footer_note

OUT = Path(__file__).resolve().parent.parent
PDF_SRC = Path(__file__).resolve().parent / "_pdf_src"
FICTION = ("Tài liệu nháp dùng cho workshop Copilot. Đơn vị, tên nhân vật, người bệnh, đối tác và số liệu đều là giả định, "
           "không phải văn bản của bất kỳ tổ chức có thật nào.")


# ============================================================ Lab 2 Bài 1-2: thông báo lịch trực Tết (nháp, lủng củng)
def tet_roster():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "THÔNG BÁO LỊCH TRỰC TẾT NGUYÊN ĐÁN ĐINH MÙI 2027",
          "Phòng Hành chính - Nhân sự  |  Bản nháp lần 2, ngày 18/11/2026")
    para(doc, "Kính gửi: Ban Giám đốc các bệnh viện, Trưởng khoa, Điều dưỡng trưởng khoa và toàn thể nhân viên "
              "tại 4 cơ sở A, B, C và D.")
    para(doc, "Căn cứ kế hoạch hoạt động năm 2026 và thông báo nghỉ Tết của Nhà nước, cũng như căn cứ vào tình hình "
              "thực tế lượng người bệnh, sản phụ dự kiến sinh trong dịp Tết theo số liệu các năm trước tại các cơ sở, "
              "Phòng Hành chính - Nhân sự xin thông báo đến toàn thể anh chị em về việc nghỉ Tết và lịch trực Tết như sau.")
    para(doc, "Như anh chị em đã biết thì bệnh viện là đơn vị hoạt động liên tục 24/7 nên trong dịp Tết vẫn phải đảm bảo "
              "đầy đủ nhân lực để tiếp nhận và điều trị người bệnh, đặc biệt là các khoa Cấp cứu, Sản, Nhi - Sơ sinh, "
              "Gây mê hồi sức và Xét nghiệm, Chẩn đoán hình ảnh, Dược là các khoa không thể gián đoạn được, do vậy "
              "việc phân ca trực cần được thực hiện sớm và các khoa cần gửi danh sách trực về Phòng Hành chính - Nhân sự "
              "trước ngày 15/12/2026 để tổng hợp trình Ban Giám đốc duyệt, các khoa gửi trễ thì sẽ ảnh hưởng tới việc "
              "tổng hợp chung của toàn hệ thống và việc chi trả phụ cấp trực Tết cũng sẽ bị chậm theo, ngoài ra các khoa "
              "cũng lưu ý là mỗi nhân viên không trực quá 3 ca trong 7 ngày Tết, ưu tiên cho nhân viên ở xa quê được về "
              "quê ăn Tết nếu có thể sắp xếp được, và nhân viên đã trực Tết năm 2026 thì năm nay sẽ được ưu tiên nghỉ trước "
              "nếu khoa có đủ người, trường hợp khoa không đủ người thì Trưởng khoa báo về Phòng Điều dưỡng để điều phối "
              "nhân lực giữa các khoa hoặc giữa các cơ sở với nhau.")
    doc.add_heading("1. Thời gian nghỉ Tết", 1)
    para(doc, "Khối hành chính nghỉ từ thứ Năm 04/02/2027 đến hết thứ Tư 10/02/2027 (mùng 5 Tết), đi làm lại vào "
              "thứ Năm 11/02/2027. Khối chuyên môn làm việc theo lịch trực của khoa. Phòng khám ngoại trú tạm nghỉ từ "
              "05/02 đến 09/02/2027; khoa Cấp cứu, phòng sinh và các khoa nội trú hoạt động bình thường.")
    doc.add_heading("2. Nguyên tắc phân ca", 1)
    bullets(doc, [
        "Mỗi ca trực gồm tối thiểu 01 bác sĩ, 02 điều dưỡng hoặc nữ hộ sinh tại mỗi khoa lâm sàng trọng yếu.",
        "Mỗi nhân viên trực không quá 3 ca trong 7 ngày nghỉ Tết.",
        "Ưu tiên nghỉ cho nhân viên đã trực Tết 2026 và nhân viên ở xa quê.",
        "Trực lãnh đạo: mỗi cơ sở có 01 thành viên Ban Giám đốc trực mỗi ngày.",
    ])
    doc.add_heading("3. Bảng trực lãnh đạo và đầu mối tại 4 cơ sở", 1)
    table(doc, ["Cơ sở", "04-05/02 (trước Tết)", "06-08/02 (mùng 1-3)", "09-10/02 (mùng 4-5)", "Đầu mối điều phối"], [
        ["Cơ sở A", "BS. Huỳnh Văn Phúc", "BS. Lâm Kim Thoa", "BS. Huỳnh Văn Phúc", "ĐD. Trương Mỹ Linh - máy lẻ 3102"],
        ["Cơ sở B", "BS. Thạch Minh Đức", "BS. Lâm Thị Hồng", "BS. Thạch Minh Đức", "ĐD. Sơn Thị Diễm - máy lẻ 4108"],
        ["Cơ sở C", "BS. Võ Hoàng Long", "BS. Đặng Ngọc Hân", "BS. Võ Hoàng Long", "ĐD. Lý Bảo Ngọc - máy lẻ 2105"],
        ["Cơ sở D", "BS. Lê Minh Tâm", "BS. Trần Quốc Huy", "BS. Nguyễn Thanh Vân", "ĐD. Phạm Thu Mai - máy lẻ 1201"],
    ], [3.2, 3.2, 3.2, 3.2, 4.4])
    doc.add_heading("4. Phụ cấp trực Tết", 1)
    para(doc, "Phụ cấp trực các ngày từ mùng 1 đến mùng 3 Tết được tính gấp 3 lần mức phụ cấp trực thường, các ngày còn "
              "lại gấp 2 lần, theo Chính sách Nhân sự hiện hành. Phụ cấp được chi trả cùng kỳ lương tháng 3/2027.")
    doc.add_heading("5. Liên hệ", 1)
    para(doc, "Mọi thắc mắc vui lòng liên hệ Phòng Hành chính - Nhân sự, chị Nguyễn Hoài An, máy lẻ 1010, "
              "hoặc đầu mối điều phối tại từng cơ sở như bảng trên.")
    doc.save(OUT / "Thông báo lịch trực Tết 2027.docx")


# ============================================================ Lab 2 Bài 3: hướng dẫn chăm sóc mẹ sau sinh (văn phong chuyên môn)
def postpartum():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "HƯỚNG DẪN CHĂM SÓC SẢN PHỤ GIAI ĐOẠN HẬU SẢN",
          "Khoa Sản - Bản nháp phát cho người bệnh  |  Nội dung chuyên môn đã được BS. Trưởng khoa Sản duyệt (giả định)")
    para(doc, "Tài liệu này áp dụng cho sản phụ sau sinh thường hoặc sau mổ lấy thai, trong giai đoạn hậu sản "
              "(6 tuần đầu sau sinh), nhằm hướng dẫn theo dõi và tự chăm sóc tại nhà sau khi xuất viện.")
    doc.add_heading("1. Theo dõi co hồi tử cung và sản dịch", 1)
    para(doc, "Sau sổ nhau, tử cung co hồi dần, đáy tử cung giảm khoảng 1 cm mỗi ngày và thường không sờ thấy trên "
              "khớp vệ sau 10 đến 14 ngày. Hiện tượng đau bụng do cơn co tử cung (cơn đau dạ con) có thể tăng khi cho "
              "con bú do tác dụng của oxytocin nội sinh. Sản dịch giai đoạn đầu là lochia rubra (đỏ sẫm, 3 đến 4 ngày), "
              "sau đó chuyển sang lochia serosa (hồng nhạt) và lochia alba (trắng ngà), kéo dài đến khoảng 4 đến 6 tuần. "
              "Sản dịch có mùi tanh nồng nhưng không hôi.")
    doc.add_heading("2. Chăm sóc vết khâu tầng sinh môn và vết mổ", 1)
    para(doc, "Với sản phụ có cắt và khâu tầng sinh môn, vệ sinh vùng sinh dục ngoài bằng nước sạch sau mỗi lần đi vệ "
              "sinh, lau khô từ trước ra sau, thay băng vệ sinh tối thiểu 4 đến 6 lần mỗi ngày. Chỉ khâu tự tiêu thường "
              "tiêu trong 10 đến 14 ngày. Với sản phụ mổ lấy thai, giữ vết mổ khô, không tự ý bóc băng khi chưa có chỉ định, "
              "theo dõi các dấu hiệu nhiễm trùng vết mổ như sưng nề, tấy đỏ, chảy dịch hoặc mủ.")
    doc.add_heading("3. Nuôi con bằng sữa mẹ", 1)
    para(doc, "Khuyến khích cho trẻ bú sớm trong giờ đầu sau sinh, bú mẹ hoàn toàn trong 6 tháng đầu và bú theo nhu cầu, "
              "trung bình 8 đến 12 lần mỗi 24 giờ. Đảm bảo tư thế và khớp ngậm đúng để phòng ngừa nứt đầu vú. "
              "Khi có hiện tượng cương tức tuyến vú, chườm ấm, xoa bóp nhẹ và cho trẻ bú hoặc vắt sữa thường xuyên.")
    doc.add_heading("4. Dinh dưỡng và vận động", 1)
    para(doc, "Sản phụ cần bổ sung năng lượng khoảng 500 kcal mỗi ngày so với bình thường, uống đủ 2 đến 2,5 lít nước, "
              "duy trì viên sắt và canxi theo chỉ định. Khuyến khích vận động sớm sau 6 đến 8 giờ với sinh thường và sau "
              "24 giờ với mổ lấy thai để giảm nguy cơ huyết khối tĩnh mạch sâu. Kiêng quan hệ tình dục ít nhất 6 tuần.")
    doc.add_heading("5. Sức khỏe tinh thần", 1)
    para(doc, "Khoảng 50 đến 80% sản phụ có thể trải qua trạng thái buồn chán sau sinh (baby blues) trong 2 tuần đầu. "
              "Nếu các triệu chứng buồn bã, mất ngủ, lo âu kéo dài trên 2 tuần, cần được đánh giá trầm cảm sau sinh. "
              "Gia đình nên hỗ trợ sản phụ nghỉ ngơi và chia sẻ việc chăm sóc trẻ.")
    doc.add_heading("6. Tái khám", 1)
    para(doc, "Tái khám sau 1 tuần với sản phụ mổ lấy thai để kiểm tra vết mổ, và tái khám hậu sản sau 6 tuần cho tất cả "
              "sản phụ để đánh giá co hồi tử cung, tư vấn biện pháp tránh thai và tầm soát các vấn đề sức khỏe sau sinh.")
    doc.add_heading("7. Dấu hiệu cần quay lại bệnh viện ngay", 1)
    bullets(doc, [
        "Ra huyết âm đạo nhiều, thấm ướt hơn 1 băng vệ sinh trong 1 giờ, hoặc ra cục máu đông lớn.",
        "Sốt từ 38 độ C trở lên, hoặc sản dịch có mùi hôi.",
        "Đau bụng dữ dội, hoặc đau tăng dần không giảm khi nghỉ ngơi.",
        "Vết mổ hoặc vết khâu sưng đỏ, chảy dịch, chảy mủ hoặc bị hở.",
        "Đau đầu dữ dội, nhìn mờ, co giật.",
        "Khó thở, đau ngực.",
        "Một bên bắp chân sưng, nóng, đỏ, đau.",
        "Vú sưng đỏ, đau nhiều kèm sốt.",
        "Buồn bã, lo âu kéo dài, hoặc có ý nghĩ làm hại bản thân hay em bé.",
    ])
    para(doc, "Khi có một trong các dấu hiệu trên, gọi đường dây nóng của bệnh viện hoặc đến khoa Cấp cứu gần nhất.",
         italic=True)
    doc.save(OUT / "Hướng dẫn chăm sóc mẹ sau sinh (nháp).docx")


# ============================================================ Lab 4: tài liệu đào tạo Phụng sự từ tâm
def culture():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "PHỤNG SỰ TỪ TÂM",
          "Tài liệu đào tạo văn hóa dành cho điều dưỡng mới  |  Phòng Điều dưỡng  |  Bản dùng cho workshop")
    doc.add_heading("1. Câu chuyện của chúng ta", 1)
    para(doc, "Hệ thống bắt đầu từ một bệnh viện chuyên sâu về sản phụ khoa và nhi với mong muốn mang dịch vụ y tế "
              "chất lượng quốc tế đến gần hơn với người dân trong vùng. Từ đó đến nay, hệ thống đã phát triển thành 4 cơ sở. "
              "Điều không thay đổi qua từng chặng đường là tinh thần Phụng sự từ tâm: mỗi người bệnh được chăm sóc "
              "như người thân của mình.")
    doc.add_heading("2. Sáu giá trị cốt lõi", 1)
    table(doc, ["Giá trị", "Ý nghĩa", "Biểu hiện trong công việc của điều dưỡng"], [
        ["Tận tâm", "Đặt người bệnh vào trung tâm", "Chủ động hỏi han, không để người bệnh phải chờ mà không được giải thích"],
        ["An toàn", "Không gây hại cho người bệnh", "Tuân thủ 6 mục tiêu an toàn người bệnh, xác định đúng người bệnh trước mọi thủ thuật"],
        ["Chuyên nghiệp", "Làm đúng, làm đủ, làm đẹp", "Trang phục chỉnh tề, thao tác chuẩn, ghi chép hồ sơ đầy đủ"],
        ["Tôn trọng", "Tôn trọng người bệnh và đồng nghiệp", "Giữ riêng tư, bảo mật thông tin, xin phép trước khi thăm khám"],
        ["Hợp tác", "Cùng nhau vì người bệnh", "Bàn giao đầy đủ giữa các ca và các khoa, hỗ trợ đồng nghiệp khi quá tải"],
        ["Cải tiến", "Mỗi ngày tốt hơn hôm qua", "Báo cáo sự cố không trừng phạt, đề xuất cải tiến quy trình"],
    ], [3, 4.5, 9])
    doc.add_heading("3. Quy tắc giao tiếp với người bệnh", 1)
    bullets(doc, [
        ("Chào và giới thiệu: ", "chào người bệnh, giới thiệu tên và vai trò của mình trước khi chăm sóc."),
        ("Giải thích trước khi làm: ", "nói rõ sắp làm gì, mất bao lâu, người bệnh cần phối hợp thế nào."),
        ("Lắng nghe: ", "để người bệnh nói hết, nhắc lại ý chính để xác nhận đã hiểu đúng."),
        ("Dùng ngôn ngữ dễ hiểu: ", "tránh thuật ngữ chuyên môn, nếu cần thì giải thích bằng ví dụ gần gũi."),
        ("Thấu cảm: ", "ghi nhận cảm xúc của người bệnh trước khi đưa ra thông tin, ví dụ \"Chị lo là đúng thôi\"."),
        ("Thông báo thời gian chờ: ", "khi người bệnh phải chờ, báo thời gian dự kiến và cập nhật nếu có thay đổi."),
        ("Bảo mật: ", "không trao đổi thông tin người bệnh ở hành lang, thang máy hay trên mạng xã hội."),
    ])
    doc.add_heading("4. Xử lý khi người bệnh không hài lòng", 1)
    para(doc, "Áp dụng 4 bước: Lắng nghe - Xin lỗi về trải nghiệm chưa tốt - Giải quyết hoặc chuyển đúng người có thẩm quyền - "
              "Theo dõi và phản hồi lại cho người bệnh. Mọi góp ý được ghi nhận vào hệ thống phản hồi trong ngày.")
    doc.add_heading("5. Tình huống thực hành", 1)
    bullets(doc, [
        "Sản phụ lần đầu sinh con lo lắng vì chưa có sữa ngay sau sinh.",
        "Người nhà phàn nàn vì chờ thủ tục xuất viện quá lâu.",
        "Người bệnh hỏi kết quả xét nghiệm khi bác sĩ chưa đọc kết quả.",
    ])
    doc.save(OUT / "Tài liệu đào tạo Phụng sự từ tâm.docx")




# ============================================================ Lab 1, 4, 7: kế hoạch 2027
# Cố ý KHÔNG đề cập: quá tải Cơ sở D / Cơ sở B còn trống, chi phí vật tư vượt 27%, thời gian chờ xuất viện.
def plan_2027():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "KẾ HOẠCH HOẠT ĐỘNG NĂM 2027 - HỆ THỐNG 4 CƠ SỞ",
          "Dự thảo v0.3 ngày 05/11/2026  |  Phòng Kế hoạch tổng hợp  |  Lưu hành nội bộ")
    doc.add_heading("1. Bối cảnh", 1)
    para(doc, "Năm 2026, hệ thống 4 cơ sở A, B, C và D duy trì tăng trưởng số ca sinh và lượt khám ngoại trú. "
              "Hai vấn đề nổi bật được ghi nhận qua 9 tháng là tỷ lệ nghỉ việc của điều dưỡng cao hơn mặt bằng ngành "
              "và điểm hài lòng người bệnh tại Cơ sở C giảm trong quý 3.")
    doc.add_heading("2. Mục tiêu năm 2027", 1)
    table(doc, ["Chỉ tiêu", "Ước 2026", "Mục tiêu 2027"], [
        ["Tổng số ca sinh toàn hệ thống", "16.200", "17.500"],
        ["Tỷ lệ nghỉ việc điều dưỡng", "18%", "Không quá 12%"],
        ["Điểm hài lòng người bệnh tại Cơ sở C (thang 5)", "4,1", "Từ 4,5 trở lên"],
        ["Tỷ lệ người bệnh đặt lịch khám trực tuyến", "22%", "40%"],
        ["Tiết đào tạo liên tục bình quân / điều dưỡng / năm", "20 tiết", "Từ 24 tiết trở lên"],
    ], [8.5, 3.5, 4.5])
    doc.add_heading("3. Nhóm giải pháp", 1)
    doc.add_heading("3.1. Giữ chân và phát triển đội ngũ điều dưỡng", 2)
    bullets(doc, [
        "Điều chỉnh phụ cấp trực đêm và phụ cấp thâm niên cho điều dưỡng từ quý 1/2027.",
        "Xây dựng lộ trình nghề nghiệp 4 bậc cho điều dưỡng, xét nâng bậc mỗi năm.",
        "Chương trình kèm cặp: mỗi điều dưỡng mới có 1 điều dưỡng hướng dẫn trong 3 tháng đầu.",
        "Khảo sát mức độ gắn kết nhân viên 2 lần mỗi năm, phỏng vấn nghỉ việc 100% trường hợp.",
    ])
    doc.add_heading("3.2. Nâng cao trải nghiệm người bệnh tại Cơ sở C", 2)
    bullets(doc, [
        "Đào tạo Phụng sự từ tâm cho 100% nhân viên tiếp xúc người bệnh tại Cơ sở C trong quý 1/2027.",
        "Bố trí điều phối viên chăm sóc khách hàng tại khu vực tiếp đón và khoa Sản.",
        "Thu thập phản hồi người bệnh qua mã QR sau mỗi lượt khám và xử lý góp ý trong 48 giờ.",
    ])
    doc.add_heading("3.3. Chuyển đổi số", 2)
    bullets(doc, [
        "Mở rộng đặt lịch khám trực tuyến và nhắc lịch tái khám qua ứng dụng.",
        "Triển khai Microsoft 365 Copilot cho khối hành chính, chăm sóc khách hàng và quản lý khoa.",
    ])
    doc.add_heading("3.4. Chất lượng và an toàn người bệnh", 2)
    bullets(doc, [
        "Duy trì các tiêu chuẩn chất lượng quốc tế, chuẩn bị tái thẩm định theo kế hoạch.",
        "Chuẩn hóa quy trình bàn giao người bệnh giữa các khoa trên toàn hệ thống.",
        "Khuyến khích báo cáo sự cố an toàn không trừng phạt, phản hồi người báo cáo trong 7 ngày.",
    ])
    doc.add_heading("4. Ngân sách dự kiến cho các giải pháp", 1)
    table(doc, ["Nhóm giải pháp", "Ngân sách (tỷ đồng)", "Đơn vị chủ trì"], [
        ["Giữ chân và phát triển điều dưỡng", "9,5", "Phòng Nhân sự, Phòng Điều dưỡng"],
        ["Trải nghiệm người bệnh tại Cơ sở C", "3,2", "Ban Giám đốc Cơ sở C, Phòng CSKH"],
        ["Chuyển đổi số", "6,8", "Phòng Công nghệ thông tin"],
        ["Chất lượng và an toàn người bệnh", "2,5", "Phòng Quản lý chất lượng"],
        ["Tổng", "22,0", ""],
    ], [7, 3.5, 6])
    doc.add_heading("5. Lộ trình triển khai", 1)
    table(doc, ["Thời gian", "Việc chính"], [
        ["Quý 1/2027", "Áp dụng phụ cấp mới, khởi động kèm cặp điều dưỡng mới, đào tạo Phụng sự từ tâm tại Cơ sở C"],
        ["Quý 2/2027", "Lộ trình nghề nghiệp 4 bậc, mở rộng đặt lịch trực tuyến, khảo sát gắn kết lần 1"],
        ["Quý 3/2027", "Chuẩn hóa phiếu bàn giao toàn hệ thống, rà soát giữa năm"],
        ["Quý 4/2027", "Khảo sát gắn kết lần 2, đánh giá kết quả và lập kế hoạch 2028"],
    ], [3.5, 13])
    doc.add_heading("6. Tiến độ phê duyệt", 1)
    para(doc, "Dự thảo được gửi các cơ sở và khoa phòng lấy ý kiến đến ngày 30/11/2026, trình Hội đồng quản trị "
              "phê duyệt trong tháng 12/2026. Góp ý gửi về Phòng Kế hoạch tổng hợp.")
    doc.save(OUT / "Kế hoạch Hoạt động 2027 (dự thảo).docx")


# ============================================================ Lab 2: dự thảo hợp đồng cung ứng vật tư (lệch chính sách)
# Điểm lệch so với Chính sách Mua sắm: tạm ứng 50% không bảo lãnh (tối đa 30% + bảo lãnh), phạt chậm 0,05%/ngày tối đa 5%
# (tối thiểu 0,1%/ngày, trần 8%), không có điều khoản thu hồi lô lỗi, mới 2 báo giá (cần 3).
# Giá trị 7,8 tỷ: thuộc thẩm quyền Tổng Giám đốc sau khi Pháp chế rà soát (từ 5 tỷ).
def supply_contract():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "HỢP ĐỒNG CUNG ỨNG VẬT TƯ Y TẾ TIÊU HAO",
          "Số: 2711/2026/HĐCU-CSD  |  Dự thảo v0.1 ngày 10/11/2026  |  Lưu hành nội bộ")
    bullets(doc, [
        ("Bên A - Bên mua: ", "Bệnh viện Cơ sở D (giả định); đại diện bởi Ông Lê Văn Khải, Phó Giám đốc phụ trách hậu cần."),
        ("Bên B - Bên bán: ", "Công ty TNHH Thiết bị Y tế Minh An (giả định); đại diện bởi Bà Trịnh Ngọc Diệp, Giám đốc."),
    ], style="Normal")
    doc.add_heading("Điều 1. Hàng hóa", 1)
    table(doc, ["Nhóm hàng", "Đơn vị", "Số lượng / 12 tháng", "Thành tiền (đồng)"], [
        ["Găng tay khám và găng phẫu thuật vô khuẩn", "Đôi", "480.000", "2.160.000.000"],
        ["Bơm kim tiêm, dây truyền dịch", "Cái", "350.000", "1.890.000.000"],
        ["Gạc, bông, băng vô khuẩn", "Gói", "120.000", "1.320.000.000"],
        ["Chỉ khâu phẫu thuật tự tiêu", "Tép", "36.000", "2.430.000.000"],
        ["Tổng giá trị hợp đồng (chưa VAT)", "", "", "7.800.000.000"],
    ], [7, 2, 3.5, 4])
    doc.add_heading("Điều 2. Giao hàng", 1)
    bullets(doc, [
        "2.1. Bên B giao hàng theo đơn đặt hàng hằng tháng của Bên A, trong vòng 05 ngày làm việc kể từ ngày nhận đơn.",
        "2.2. Hàng giao có hạn sử dụng còn lại tối thiểu 12 tháng, kèm chứng nhận chất lượng (CO, CQ) của từng lô.",
        "2.3. Địa điểm giao hàng: Kho vật tư, Bệnh viện Cơ sở D.",
    ], style="Normal")
    doc.add_heading("Điều 3. Thanh toán", 1)
    bullets(doc, [
        "3.1. Bên A tạm ứng cho Bên B 50% tổng giá trị hợp đồng trong vòng 07 ngày kể từ ngày ký.",
        "3.2. Phần còn lại thanh toán theo từng đợt giao hàng, trong vòng 30 ngày kể từ ngày nhận đủ hàng và hóa đơn hợp lệ.",
    ], style="Normal")
    doc.add_heading("Điều 4. Chất lượng và bảo hành", 1)
    bullets(doc, [
        "4.1. Hàng hóa mới 100%, đúng chủng loại, có số đăng ký lưu hành còn hiệu lực.",
        "4.2. Bên B đổi hàng không đạt chất lượng phát hiện khi kiểm nhập trong vòng 10 ngày làm việc.",
    ], style="Normal")
    doc.add_heading("Điều 5. Phạt vi phạm", 1)
    bullets(doc, [
        "5.1. Giao hàng chậm: Bên B chịu phạt 0,05% giá trị đơn hàng giao chậm cho mỗi ngày chậm, tối đa 5% giá trị đơn hàng.",
        "5.2. Giao hàng không đúng chủng loại: Bên B đổi hàng và chịu chi phí vận chuyển phát sinh.",
    ], style="Normal")
    doc.add_heading("Điều 6. Hiệu lực", 1)
    para(doc, "Hợp đồng có hiệu lực 12 tháng kể từ ngày ký, được lập thành 04 bản, mỗi bên giữ 02 bản có giá trị như nhau.")
    doc.add_heading("Ghi chú của người soạn thảo (xóa trước khi ký)", 1)
    bullets(doc, [
        "Đã nhận 02 báo giá (Minh An và một nhà cung cấp khác), Minh An rẻ hơn khoảng 4%.",
        "Minh An đề nghị tạm ứng 50% vì phải nhập hàng trước, chưa đồng ý cung cấp bảo lãnh tạm ứng.",
        "Khoa Sản và Phòng mổ cần bắt đầu nhận hàng từ 01/12/2026 nên mong ký trước 25/11.",
    ], style="Normal")
    doc.save(OUT / "Dự thảo Hợp đồng cung ứng vật tư.docx")


# ============================================================ Lab 2: chính sách mua sắm (PDF)
def procurement_policy():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "CHÍNH SÁCH MUA SẮM NỘI BỘ", "Bản giả định cho workshop  |  Mã CS-MS-02, phiên bản 3.0, hiệu lực 01/01/2026")
    doc.add_heading("Mục 1. Phạm vi", 1)
    para(doc, "Chính sách áp dụng cho mọi hoạt động mua sắm thuốc, vật tư y tế, trang thiết bị và dịch vụ tại các cơ sở "
              "thuộc hệ thống.")
    doc.add_heading("Mục 2. Lựa chọn nhà cung cấp", 1)
    bullets(doc, [
        "2.1. Gói mua sắm từ 100 triệu đồng phải có tối thiểu 03 báo giá độc lập.",
        "2.2. Nhà cung cấp vật tư y tế phải có số đăng ký lưu hành còn hiệu lực cho từng mặt hàng.",
    ])
    doc.add_heading("Mục 3. Thẩm quyền phê duyệt", 1)
    table(doc, ["Giá trị gói mua sắm", "Cấp phê duyệt"], [
        ["Dưới 100 triệu đồng", "Trưởng phòng Vật tư - Thiết bị"],
        ["Từ 100 triệu đến dưới 1 tỷ đồng", "Phó Giám đốc phụ trách hậu cần"],
        ["Từ 1 tỷ đến dưới 5 tỷ đồng", "Giám đốc cơ sở"],
        ["Từ 5 tỷ đồng trở lên", "Tổng Giám đốc, sau khi Phòng Pháp chế rà soát hợp đồng"],
    ], [7, 9])
    doc.add_heading("Mục 4. Điều khoản bắt buộc trong hợp đồng", 1)
    bullets(doc, [
        ("4.1. Tạm ứng: ", "tối đa 30% giá trị hợp đồng và phải có bảo lãnh tạm ứng của ngân hàng tương ứng. "
                          "Mức cao hơn là ngoại lệ, cần Tổng Giám đốc phê duyệt."),
        ("4.2. Phạt chậm giao: ", "tối thiểu 0,1% giá trị phần giao chậm cho mỗi ngày chậm, mức phạt tối đa 8% giá trị phần vi phạm."),
        ("4.3. Thu hồi lô lỗi: ", "hợp đồng vật tư y tế phải có điều khoản thu hồi. Khi có thông báo thu hồi của nhà sản xuất "
                                 "hoặc cơ quan quản lý, hoặc khi bệnh viện phát hiện lô hàng lỗi, nhà cung cấp phải thu hồi "
                                 "và thay thế trong 48 giờ, chịu toàn bộ chi phí phát sinh."),
        ("4.4. Truy xuất: ", "mỗi lô hàng phải ghi số lô, hạn dùng và kèm chứng nhận chất lượng."),
        ("4.5. Thanh toán: ", "trong vòng 30 ngày kể từ ngày nghiệm thu và nhận hóa đơn hợp lệ."),
    ])
    doc.add_heading("Mục 5. Rà soát pháp chế", 1)
    para(doc, "Hợp đồng có điều khoản khác với Mục 4 phải được Phòng Pháp chế rà soát và ghi rõ lý do ngoại lệ trong tờ trình.")
    PDF_SRC.mkdir(exist_ok=True)
    doc.save(PDF_SRC / "Chính sách Mua sắm nội bộ.docx")


# ============================================================ Lab 7: chính sách nhân sự (PDF, knowledge source)
def hr_policy():
    doc = new_doc()
    footer_note(doc, FICTION)
    title(doc, "CHÍNH SÁCH NHÂN SỰ", "Bản giả định cho workshop  |  Mã CS-NS-01, phiên bản 5.1, hiệu lực 01/07/2026")
    doc.add_heading("Mục 1. Phạm vi áp dụng", 1)
    para(doc, "Áp dụng cho toàn bộ nhân viên ký hợp đồng lao động với các cơ sở và văn phòng điều hành.")
    doc.add_heading("Mục 2. Thời giờ làm việc, ca trực và đổi ca", 1)
    bullets(doc, [
        "2.1. Khối hành chính: 8 giờ/ngày, từ thứ Hai đến sáng thứ Bảy.",
        "2.2. Khối chuyên môn làm việc theo ca: ca ngày 7:00-19:00, ca đêm 19:00-7:00, theo lịch của khoa.",
        "2.3. Mỗi nhân viên trực đêm không quá 8 ca/tháng, trừ trường hợp được Giám đốc cơ sở chấp thuận.",
        "2.4. Đổi ca: hai nhân viên cùng chức danh tự thỏa thuận, gửi đề nghị trên hệ thống nhân sự và được Điều dưỡng "
        "trưởng khoa duyệt trước ít nhất 24 giờ. Không đổi ca nếu khiến một người làm liên tục quá 24 giờ.",
        "2.5. Giờ làm thêm không quá 40 giờ/tháng và 300 giờ/năm; được trả lương làm thêm theo quy định pháp luật.",
    ])
    doc.add_heading("Mục 3. Nghỉ phép năm", 1)
    bullets(doc, [
        "3.1. Nhân viên làm việc đủ 12 tháng được nghỉ 12 ngày phép năm hưởng nguyên lương.",
        "3.2. Cứ đủ 5 năm làm việc được cộng thêm 1 ngày phép (ví dụ: 5 năm được 13 ngày, 10 năm được 14 ngày).",
        "3.3. Phép năm chưa dùng hết được chuyển tối đa 5 ngày sang năm sau và phải dùng trước ngày 31/03.",
        "3.4. Đăng ký nghỉ phép trên hệ thống nhân sự trước ít nhất 3 ngày làm việc, trừ trường hợp đột xuất.",
        "3.5. Không đăng ký nghỉ phép trong 7 ngày nghỉ Tết Nguyên đán nếu đã có tên trong lịch trực Tết.",
    ])
    doc.add_heading("Mục 4. Nghỉ việc riêng", 1)
    table(doc, ["Trường hợp", "Số ngày nghỉ hưởng nguyên lương"], [
        ["Bản thân kết hôn", "03 ngày"],
        ["Con đẻ, con nuôi kết hôn", "01 ngày"],
        ["Cha, mẹ (hai bên), vợ hoặc chồng, con chết", "03 ngày"],
    ], [8, 8.5])
    doc.add_heading("Mục 5. Phụ cấp trực", 1)
    table(doc, ["Đối tượng", "Trực đêm ngày thường", "Trực đêm cuối tuần", "Trực ngày lễ, Tết"], [
        ["Bác sĩ", "500.000 đồng/ca", "650.000 đồng/ca", "Gấp 3 mức ngày thường"],
        ["Điều dưỡng, nữ hộ sinh, kỹ thuật viên", "300.000 đồng/ca", "400.000 đồng/ca", "Gấp 3 mức ngày thường"],
        ["Nhân viên hỗ trợ", "200.000 đồng/ca", "260.000 đồng/ca", "Gấp 3 mức ngày thường"],
    ], [5.5, 3.6, 3.6, 3.8])
    bullets(doc, [
        "5.1. Mức gấp 3 áp dụng từ mùng 1 đến mùng 3 Tết Nguyên đán và các ngày lễ; các ngày nghỉ Tết còn lại áp dụng gấp 2.",
        "5.2. Phụ cấp được chi trả cùng kỳ lương tháng kế tiếp, căn cứ bảng chấm công đã được Trưởng khoa xác nhận.",
    ])
    doc.add_heading("Mục 6. Đào tạo liên tục", 1)
    bullets(doc, [
        "6.1. Người hành nghề khám bệnh, chữa bệnh phải hoàn thành tối thiểu 48 tiết đào tạo liên tục trong mỗi chu kỳ 2 năm.",
        "6.2. Tiết học được ghi nhận khi có chứng nhận của Phòng Đào tạo hoặc đơn vị đào tạo được công nhận.",
        "6.3. Hệ thống hỗ trợ 100% học phí các khóa đào tạo bắt buộc và 50% học phí khóa nâng cao được Trưởng khoa đề xuất.",
        "6.4. Nhân viên được hỗ trợ học phí khóa trên 20 triệu đồng cam kết làm việc tối thiểu 24 tháng sau khi hoàn thành khóa học.",
    ])
    doc.add_heading("Mục 7. Thẩm quyền phê duyệt", 1)
    table(doc, ["Nội dung", "Cấp phê duyệt"], [
        ["Nghỉ phép đến 3 ngày", "Điều dưỡng trưởng khoa (điều dưỡng) hoặc Trưởng khoa (bác sĩ)"],
        ["Nghỉ phép trên 3 ngày đến 10 ngày", "Trưởng khoa"],
        ["Nghỉ phép trên 10 ngày, nghỉ không lương", "Giám đốc cơ sở"],
        ["Đổi ca trực", "Điều dưỡng trưởng khoa, đề nghị trước 24 giờ"],
        ["Trực đêm quá 8 ca/tháng", "Giám đốc cơ sở"],
        ["Cử đi đào tạo ngoài bệnh viện", "Trưởng khoa đề xuất, Giám đốc cơ sở duyệt"],
    ], [7, 9])
    doc.add_heading("Mục 8. Bảo mật thông tin", 1)
    para(doc, "Nhân viên không gửi thông tin cá nhân của mình hoặc của người khác (số CCCD, số tài khoản, thông tin sức khỏe) "
              "qua tin nhắn, email hay công cụ AI. Mọi yêu cầu liên quan đến lương, kỷ luật của cá nhân liên hệ trực tiếp "
              "Phòng Nhân sự.")
    doc.add_heading("Mục 9. Liên hệ", 1)
    para(doc, "Phòng Nhân sự: máy lẻ 1010, hộp thư nhansu@benhvien.example. Tại mỗi cơ sở, liên hệ "
              "bộ phận Hành chính - Nhân sự của cơ sở.")
    PDF_SRC.mkdir(exist_ok=True)
    doc.save(PDF_SRC / "Chính sách Nhân sự.docx")


if __name__ == "__main__":
    for f in (tet_roster, postpartum, culture, plan_2027, supply_contract, procurement_policy, hr_policy):
        f()
        print("ok", f.__name__)
