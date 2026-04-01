PAPER_METADATA = {
    "title": "DNA Sequence Classification Using Machine Learning Models Based on k-mer Features",
    "author": "Afthar Kautsar",
    "journal": "Journal of Computers and Digital Business (JCBD)",
    "issue": "Volume 4, Number 2, May 2025, pages 100-105",
    "doi": "https://doi.org/10.56427/jcbd.v4i2.762",
}

MODEL_RESULTS = [
    {
        "Model": "Random Forest",
        "Accuracy": 0.71,
        "Precision (normal)": 0.75,
        "Recall (normal)": 0.08,
        "Precision (mutation)": 0.71,
        "Recall (mutation)": 0.99,
    },
    {
        "Model": "SVM",
        "Accuracy": 0.70,
        "Precision (normal)": 0.00,
        "Recall (normal)": 0.00,
        "Precision (mutation)": 0.70,
        "Recall (mutation)": 1.00,
    },
    {
        "Model": "DNN",
        "Accuracy": 0.67,
        "Precision (normal)": 0.38,
        "Recall (normal)": 0.13,
        "Precision (mutation)": 0.71,
        "Recall (mutation)": 0.91,
    },
]

SAMPLE_SEQUENCES = {
    "balanced": "ATGCAATGCTTACGATACGTAGCTAACGTA",
    "mutation": "CGGCGCGGCCGCGGCGTCCGCGGGCCGCGC",
}

PAPER_COPY = {
    "en": {
        "sidebar": {
            "brand": "DNA Demo",
            "caption": "Editorial-lab walkthrough for DNA sequence classification with 3-mer features.",
            "toggle_label": "Tiếng Việt",
            "nav_title": "Navigate",
            "nav_items": [
                ("1. DNA Sequence Classification", "dna-sequence-classification"),
                ("2. Paper Context and cfDNA", "paper-context-and-cfdna"),
                ("3. Method and 3-mer Features", "method-and-3-mer-features"),
                ("4. Results and Limits", "results-and-limitations"),
                ("5. Demo DNA Sequence", "demo-dna-sequence"),
                ("6. Conclusion and Scale-up", "conclusion-and-scale-up"),
            ],
            "note": "DNA is the product scope. cfDNA appears only as the paper context.",
        },
        "hero": {
            "eyebrow": "Research exhibit / product demo",
            "title": "DNA Sequence Classification",
            "subtitle": "Read the paper like an exhibit. Explore the pipeline like a product.",
            "body": (
                "This app keeps the language centered on DNA sequence classification while showing how the paper "
                "uses cfDNA as a motivating application. The goal is clarity first, then interaction."
            ),
            "cta": "Go to DNA demo",
            "micro": "3-mer features • Random Forest / SVM / DNN • Paper-first storytelling",
            "meta_title": "Paper source",
        },
        "intro": {
            "section": "1. DNA Sequence Classification",
            "lead": (
                "DNA sequence classification turns a DNA string into a numeric representation, then asks a model "
                "to separate one class from another."
            ),
            "bullets": [
                "The paper uses 3-mer frequency vectors as the feature space.",
                "The strongest reported table result is Random Forest at 71% accuracy.",
                "The app presents the method first and keeps the demo at the DNA level.",
            ],
        },
        "paper_context": {
            "section": "2. Paper Context and cfDNA",
            "left_title": "What the paper is trying to do",
            "left_body": (
                "The paper studies whether machine learning models can classify DNA-derived fragments into normal "
                "and mutation-related groups after converting each fragment into 3-mer frequency features."
            ),
            "right_title": "How this demo frames it",
            "right_body": (
                "cfDNA remains the research context, but the product language stays on DNA sequence classification "
                "so the audience can understand the pipeline without reading it as a clinical tool."
            ),
            "callout": "Research context: cfDNA. Product demo scope: DNA sequences.",
        },
        "method": {
            "section": "3. Method and 3-mer Features",
            "lead": "The core logic is a four-step flow. Each step does one job and moves the audience closer to the prediction.",
            "steps": [
                {
                    "number": "01",
                    "title": "Read a DNA sequence",
                    "body": "The input is a string made of A, C, G, and T.",
                },
                {
                    "number": "02",
                    "title": "Extract 3-mers",
                    "body": "A sliding window of length 3 produces motifs such as ATG, TGC, and GCG.",
                },
                {
                    "number": "03",
                    "title": "Count motif frequencies",
                    "body": "The frequency profile becomes the numeric feature vector.",
                },
                {
                    "number": "04",
                    "title": "Compare model behavior",
                    "body": "The paper reports Random Forest, SVM, and DNN on the same representation.",
                },
            ],
        },
        "results": {
            "section": "4. Results and Limits",
            "takeaway": "Random Forest leads the reported table, but the experiment remains heavily biased toward the mutation class.",
            "chart_title": "Reported accuracy by model",
            "table_title": "Compact model comparison",
            "limitations_title": "Why the paper needs caution",
            "limitations": [
                "Overall accuracy hides weak performance on the normal class.",
                "All three models are much stronger on mutation than on normal DNA.",
                "The experimental setup is not documented deeply enough for clean reproducibility.",
                "Simple 3-mer features are useful for teaching, but limited for nuanced biological tasks.",
            ],
            "inconsistencies_title": "Internal inconsistencies in the paper",
            "inconsistencies": [
                {
                    "title": "Best model conflict",
                    "body": "The abstract says DNN performed best, but the tables and conclusion show Random Forest at 71% accuracy.",
                },
                {
                    "title": "Model list conflict",
                    "body": "The abstract mentions Decision Tree, SVM, and DNN, but the reported experiment uses Random Forest, SVM, and DNN.",
                },
                {
                    "title": "Dataset size conflict",
                    "body": "The abstract mentions 3,000 DNA sequences, while the methodology describes 630 DNA fragments from a 126,033 bp sequence.",
                },
            ],
        },
        "demo": {
            "section": "5. Demo DNA Sequence",
            "lead": (
                "Paste a DNA sequence, inspect the generated 3-mers, then run the lightweight demo classifier. "
                "The UI explains the pipeline before it asks you to trust the output."
            ),
            "sample_labels": {
                "balanced": "Balanced DNA sample",
                "mutation": "Mutation-leaning DNA sample",
            },
            "input_label": "Paste a DNA sequence",
            "input_help": "Only A, C, G, and T are accepted. Spaces and line breaks are ignored.",
            "run_cta": "Run demo classifier",
            "idle_note": "Load a sample or paste a DNA sequence, then run the demo classifier.",
            "workspace_title": "Workspace",
            "preview_title": "Pipeline preview",
            "cleaned_title": "Input after cleaning",
            "kmers_title": "First generated 3-mers",
            "table_title": "3-mer frequency table",
            "chart_title": "Most frequent 3-mers",
            "output_title": "Demo classifier output",
            "confidence_label": "Label confidence",
            "mutation_probability": "Mutation-like probability",
            "feature_title": "Top feature influences",
            "note": (
                "This demo classifier is illustrative. It explains the DNA to 3-mer to prediction pipeline, "
                "but it does not reproduce the paper's training setup and it is not a clinical tool."
            ),
            "helper": "DNA is the primary term here. cfDNA is only discussed in the paper context above.",
            "metrics": {
                "length": "Sequence length",
                "kmers": "Number of 3-mers",
                "unique": "Unique 3-mers",
                "label": "Predicted label",
            },
            "pipeline": ["DNA input", "3-mer extraction", "feature vector", "demo prediction"],
        },
        "footer": {
            "section": "6. Conclusion and Scale-up",
            "takeaway_title": "Main takeaway",
            "takeaway_body": (
                "The paper is useful for explaining how 3-mer features can support DNA sequence classification, "
                "but the reported results should be read with caution because the mutation class dominates performance "
                "and the manuscript contains internal inconsistencies."
            ),
            "scale_title": "Scale-up ideas",
            "ideas": [
                "Replace the demo classifier with a trained model when a curated DNA dataset is available.",
                "Add CSV upload for batch prediction and model comparison.",
                "Support multiple k values so the audience can compare richer feature spaces.",
            ],
        },
        "table_labels": {
            "Model": "Model",
            "Accuracy": "Accuracy",
            "Precision (normal)": "Precision (normal)",
            "Recall (normal)": "Recall (normal)",
            "Precision (mutation)": "Precision (mutation)",
            "Recall (mutation)": "Recall (mutation)",
            "3-mer": "3-mer",
            "Count": "Count",
            "Relative frequency": "Relative frequency",
            "feature": "Feature",
            "value": "Value",
            "impact": "Impact",
            "effect": "Effect",
            "reason": "Reason",
        },
        "prediction_labels": {
            "normal-like DNA": "normal-like DNA",
            "mutation-like DNA": "mutation-like DNA",
            "effect_mutation": "pushes toward mutation-like DNA",
            "effect_normal": "pushes toward normal-like DNA",
        },
    },
    "vi": {
        "sidebar": {
            "brand": "DNA Demo",
            "caption": "Bản trình bày kiểu editorial-lab cho bài toán phân loại chuỗi DNA bằng đặc trưng 3-mer.",
            "toggle_label": "Tiếng Việt",
            "nav_title": "Điều hướng",
            "nav_items": [
                ("1. Phân loại chuỗi DNA", "dna-sequence-classification"),
                ("2. Bối cảnh bài báo và cfDNA", "paper-context-and-cfdna"),
                ("3. Phương pháp và đặc trưng 3-mer", "method-and-3-mer-features"),
                ("4. Kết quả và giới hạn", "results-and-limitations"),
                ("5. Demo chuỗi DNA", "demo-dna-sequence"),
                ("6. Kết luận và hướng scale-up", "conclusion-and-scale-up"),
            ],
            "note": "DNA là phạm vi của sản phẩm demo. cfDNA chỉ xuất hiện như bối cảnh của bài báo.",
        },
        "hero": {
            "eyebrow": "Research exhibit / product demo",
            "title": "Phân loại chuỗi DNA",
            "subtitle": "Đọc bài báo như một bản trưng bày. Khám phá pipeline như một sản phẩm demo.",
            "body": (
                "App này giữ ngôn ngữ xoay quanh phân loại chuỗi DNA, đồng thời cho thấy cách bài báo dùng cfDNA "
                "như một bối cảnh ứng dụng. Mục tiêu là hiểu rõ phương pháp trước, rồi mới tương tác."
            ),
            "cta": "Đi tới khu vực demo DNA",
            "micro": "Đặc trưng 3-mer • Random Forest / SVM / DNN • Kể chuyện theo bài báo",
            "meta_title": "Nguồn bài báo",
        },
        "intro": {
            "section": "1. Phân loại chuỗi DNA",
            "lead": (
                "Phân loại chuỗi DNA là quá trình biến một chuỗi DNA thành biểu diễn số, rồi để mô hình tách "
                "các lớp dữ liệu khác nhau."
            ),
            "bullets": [
                "Bài báo dùng vector tần suất 3-mer làm không gian đặc trưng.",
                "Kết quả mạnh nhất trong bảng là Random Forest với accuracy 71%.",
                "App trình bày phương pháp trước và giữ phần demo ở mức DNA tổng quát.",
            ],
        },
        "paper_context": {
            "section": "2. Bối cảnh bài báo và cfDNA",
            "left_title": "Bài báo đang cố giải quyết điều gì",
            "left_body": (
                "Bài báo nghiên cứu xem các mô hình học máy có thể phân loại các mảnh DNA thành nhóm bình thường "
                "và nhóm liên quan đến đột biến sau khi chuyển từng mảnh thành vector tần suất 3-mer hay không."
            ),
            "right_title": "Cách app này đóng khung vấn đề",
            "right_body": (
                "cfDNA vẫn là bối cảnh nghiên cứu của bài báo, nhưng ngôn ngữ sản phẩm giữ ở mức phân loại chuỗi DNA "
                "để người xem hiểu pipeline mà không hiểu nhầm đây là công cụ lâm sàng."
            ),
            "callout": "Bối cảnh nghiên cứu: cfDNA. Phạm vi sản phẩm demo: chuỗi DNA.",
        },
        "method": {
            "section": "3. Phương pháp và đặc trưng 3-mer",
            "lead": "Logic cốt lõi đi theo bốn bước. Mỗi bước làm đúng một việc và đẩy người xem gần hơn tới kết quả dự đoán.",
            "steps": [
                {
                    "number": "01",
                    "title": "Đọc một chuỗi DNA",
                    "body": "Input là một chuỗi chỉ gồm A, C, G và T.",
                },
                {
                    "number": "02",
                    "title": "Tách các 3-mer",
                    "body": "Một cửa sổ trượt độ dài 3 tạo ra các motif như ATG, TGC và GCG.",
                },
                {
                    "number": "03",
                    "title": "Đếm tần suất motif",
                    "body": "Hồ sơ tần suất trở thành vector đặc trưng số.",
                },
                {
                    "number": "04",
                    "title": "So sánh hành vi mô hình",
                    "body": "Bài báo báo cáo Random Forest, SVM và DNN trên cùng một kiểu biểu diễn.",
                },
            ],
        },
        "results": {
            "section": "4. Kết quả và giới hạn",
            "takeaway": "Random Forest đứng đầu trong bảng kết quả, nhưng toàn bộ thí nghiệm vẫn lệch mạnh về lớp mutation.",
            "chart_title": "Accuracy được báo cáo theo từng mô hình",
            "table_title": "Bảng so sánh mô hình rút gọn",
            "limitations_title": "Vì sao cần đọc bài báo này một cách thận trọng",
            "limitations": [
                "Accuracy tổng thể che khuất việc mô hình yếu ở lớp normal.",
                "Cả ba mô hình đều mạnh hơn nhiều ở lớp mutation so với DNA bình thường.",
                "Thiết lập thực nghiệm chưa được mô tả đủ sâu để tái lập sạch sẽ.",
                "Đặc trưng 3-mer phù hợp cho mục tiêu giảng giải, nhưng còn hạn chế với các bài toán sinh học tinh vi hơn.",
            ],
            "inconsistencies_title": "Các điểm bất nhất ngay trong bài báo",
            "inconsistencies": [
                {
                    "title": "Mâu thuẫn về mô hình tốt nhất",
                    "body": "Abstract nói DNN tốt nhất, nhưng bảng kết quả và phần kết luận lại cho thấy Random Forest đạt accuracy 71%.",
                },
                {
                    "title": "Mâu thuẫn về danh sách mô hình",
                    "body": "Abstract nhắc đến Decision Tree, SVM và DNN, nhưng phần thực nghiệm lại dùng Random Forest, SVM và DNN.",
                },
                {
                    "title": "Mâu thuẫn về quy mô dữ liệu",
                    "body": "Abstract nói có 3.000 chuỗi DNA, trong khi phần phương pháp mô tả 630 mảnh DNA từ một chuỗi dài 126.033 bp.",
                },
            ],
        },
        "demo": {
            "section": "5. Demo chuỗi DNA",
            "lead": (
                "Dán một chuỗi DNA, quan sát các 3-mer được tạo ra, rồi chạy demo classifier. "
                "Giao diện giải thích pipeline trước khi yêu cầu người xem tin vào output."
            ),
            "sample_labels": {
                "balanced": "Mẫu DNA cân bằng",
                "mutation": "Mẫu DNA nghiêng mutation",
            },
            "input_label": "Dán chuỗi DNA",
            "input_help": "Chỉ chấp nhận A, C, G và T. Khoảng trắng và xuống dòng sẽ được bỏ qua.",
            "run_cta": "Chạy demo classifier",
            "idle_note": "Hãy nạp mẫu có sẵn hoặc dán một chuỗi DNA rồi chạy demo classifier.",
            "workspace_title": "Không gian thao tác",
            "preview_title": "Xem trước pipeline",
            "cleaned_title": "Input sau khi làm sạch",
            "kmers_title": "Các 3-mer đầu tiên được tạo ra",
            "table_title": "Bảng tần suất 3-mer",
            "chart_title": "Các 3-mer xuất hiện nhiều nhất",
            "output_title": "Kết quả từ demo classifier",
            "confidence_label": "Độ tự tin của nhãn",
            "mutation_probability": "Xác suất nghiêng mutation",
            "feature_title": "Các yếu tố ảnh hưởng mạnh nhất",
            "note": (
                "Demo classifier này chỉ nhằm mục đích minh họa. Nó giúp giải thích pipeline DNA -> 3-mer -> dự đoán, "
                "không tái lập đúng thiết lập huấn luyện của bài báo và cũng không phải công cụ lâm sàng."
            ),
            "helper": "Ở đây DNA là thuật ngữ chính. cfDNA chỉ được nhắc ở phần bối cảnh bài báo phía trên.",
            "metrics": {
                "length": "Độ dài chuỗi",
                "kmers": "Số lượng 3-mer",
                "unique": "Số 3-mer khác nhau",
                "label": "Nhãn dự đoán",
            },
            "pipeline": ["DNA input", "Tách 3-mer", "Vector đặc trưng", "Demo prediction"],
        },
        "footer": {
            "section": "6. Kết luận và hướng scale-up",
            "takeaway_title": "Ý chính cần nhớ",
            "takeaway_body": (
                "Bài báo hữu ích để giải thích cách đặc trưng 3-mer có thể hỗ trợ phân loại chuỗi DNA, "
                "nhưng kết quả cần được đọc thận trọng vì lớp mutation đang chi phối hiệu năng và bản thảo có nhiều điểm bất nhất."
            ),
            "scale_title": "Các hướng mở rộng tiếp theo",
            "ideas": [
                "Thay demo classifier bằng mô hình đã huấn luyện khi có bộ dữ liệu DNA được curate tốt.",
                "Thêm upload CSV để dự đoán hàng loạt và so sánh mô hình.",
                "Hỗ trợ nhiều giá trị k để người xem so sánh các không gian đặc trưng phong phú hơn.",
            ],
        },
        "table_labels": {
            "Model": "Mô hình",
            "Accuracy": "Accuracy",
            "Precision (normal)": "Precision (normal)",
            "Recall (normal)": "Recall (normal)",
            "Precision (mutation)": "Precision (mutation)",
            "Recall (mutation)": "Recall (mutation)",
            "3-mer": "3-mer",
            "Count": "Số lần",
            "Relative frequency": "Tần suất tương đối",
            "feature": "Đặc trưng",
            "value": "Giá trị",
            "impact": "Tác động",
            "effect": "Hướng tác động",
            "reason": "Giải thích",
        },
        "prediction_labels": {
            "normal-like DNA": "DNA nghiêng normal",
            "mutation-like DNA": "DNA nghiêng mutation",
            "effect_mutation": "đẩy kết quả về phía mutation",
            "effect_normal": "đẩy kết quả về phía normal",
        },
    },
}


def get_copy(locale: str) -> dict[str, object]:
    return PAPER_COPY["vi"] if locale == "vi" else PAPER_COPY["en"]
