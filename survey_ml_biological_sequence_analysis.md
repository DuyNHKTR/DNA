# Survey ngắn: ML cho Biological Sequence Analysis

## 1. Field này là gì, và vì sao ML hợp với biological sequences?

`Biological sequence analysis` là bài toán học từ chuỗi sinh học như `DNA`, `RNA`, và `protein` để dự đoán chức năng, motif, cấu trúc, hiệu ứng đột biến, hay nhãn sinh học ở mức gene, vùng điều hòa, hoặc phân tử. Về mặt hình thức, đây là dữ liệu tuần tự với bảng chữ cái nhỏ nhưng phụ thuộc ngữ cảnh rất dài, nên khá tự nhiên cho các họ mô hình từng thành công trong NLP như `CNN`, `RNN`, `Transformer`, rồi gần đây là `state space models` và `foundation models`.

Ba bài review/primer dưới đây là nền tốt để đặt bối cảnh:

- [An introduction to deep learning on biological sequence data: examples and solutions](https://academic.oup.com/bioinformatics/article-abstract/33/22/3685/4092933), *Bioinformatics* (2017). Bài nhập môn khá gọn, giải thích vì sao chuỗi sinh học có thể xem như đối tượng học biểu diễn, và cách `CNN/RNN` được dùng cho motif discovery, peptide binding, protein annotation.
- [Deep learning: new computational modelling techniques for genomics](https://www.nature.com/articles/s41576-019-0122-6), *Nature Reviews Genetics* (2019). Review nền cho mảng genomics, đặc biệt mạnh ở phần dự đoán tác động biến thể, chromatin accessibility, splicing, và interpretability.
- [Language models for biological research: a primer](https://www.nature.com/articles/s41592-024-02354-y), *Nature Methods* (2024). Primer mới hơn, hữu ích để hiểu bước chuyển từ supervised deep learning sang `biological language models` và `foundation models`.

Nhìn ở mức rộng, field này đi qua ba giai đoạn chính:

1. `2015-2018`: học motif và regulatory logic bằng `CNN` hoặc `CNN + RNN`.
2. `2019-2022`: chuyển sang tiền huấn luyện trên chuỗi lớn, nhất là với `protein` rồi đến `DNA`.
3. `2023-2025`: bùng nổ `foundation models`, ngữ cảnh dài, zero-shot embeddings, và benchmark liên-task.

## 2. Các nhánh bài báo chính

### 2.1. Sequence classification và motif discovery

Đây là nhánh sớm và kinh điển nhất: mô hình học mẫu cục bộ trong chuỗi để nhận diện motif, binding preference, hoặc vùng chức năng.

- [Predicting the sequence specificities of DNA- and RNA-binding proteins by deep learning](https://pubmed.ncbi.nlm.nih.gov/26213851/), *Nature Biotechnology* (2015, `DeepBind`).
  - Một trong những paper mốc đầu tiên cho thấy deep learning có thể học trực tiếp specificity của DNA/RNA-binding proteins từ chuỗi.
  - Ý tưởng quan trọng là thay các đặc trưng thủ công bằng motif learned end-to-end; đây là bước mở đầu cho rất nhiều bài sau trong regulatory sequence modeling.

- [DanQ: a hybrid convolutional and recurrent deep neural network for quantifying the function of DNA sequences](https://academic.oup.com/nar/article/44/11/e107/2468300), *Nucleic Acids Research* (2016).
  - DanQ kết hợp `CNN` để học motif cục bộ và `bi-directional LSTM` để giữ phụ thuộc dài hơn trong DNA.
  - Paper này đại diện khá rõ cho giai đoạn chuyển từ mô hình motif-based sang mô hình có khái niệm “ngữ cảnh” trong chuỗi.

### 2.2. Variant effect và regulatory genomics

Nhánh này dùng chuỗi DNA để dự đoán tác động sinh học của các biến thể không mã hóa, promoter, splice site, enhancer, hoặc tín hiệu epigenomic.

- [Predicting effects of noncoding variants with deep learning-based sequence model](https://pubmed.ncbi.nlm.nih.gov/26301843/), *Nature Methods* (2015, `DeepSEA`).
  - DeepSEA là paper kinh điển cho regulatory genomics: từ chuỗi DNA dự đoán chromatin features và suy ra tác động của noncoding variants.
  - Điểm quan trọng là nó đặt khuôn cho bài toán “sequence-to-function” trong vùng không mã hóa, vốn vẫn là trục lớn của genomics ML đến hiện nay.

- [DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome](https://academic.oup.com/bioinformatics/article/37/15/2112/6128680), *Bioinformatics* (2021).
  - Đây là một trong những paper đại diện đầu tiên đưa tư duy `BERT-style pretraining` vào DNA, thay vì chỉ huấn luyện supervised trên task riêng lẻ.
  - Điểm mạnh là cho thấy pretraining trên genome có thể transfer sang promoter prediction, splice site prediction, TF binding site prediction, và cả interpretability ở mức nucleotide.

### 2.3. Protein sequence modeling và representation transfer

Với protein, self-supervised learning thường tiến rất nhanh vì có kho sequence rất lớn và nhiều bài toán downstream rõ ràng như structure, mutational effect, remote homology.

- [Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences](https://pubmed.ncbi.nlm.nih.gov/33876751/), *PNAS* (2021).
  - Đây là paper mốc của protein language modeling ở quy mô lớn, thường được xem như nền cho dòng `ESM`.
  - Đóng góp chính là chỉ ra rằng chỉ từ sequence, biểu diễn học được đã mã hóa thông tin về structure, secondary structure, remote homology, và mutational effect.

Trong survey tổng quan này, protein được đưa vào như bằng chứng mạnh nhất cho luận điểm: `self-supervised pretraining` trên biological sequences thực sự học được biểu diễn có thể transfer, chứ không chỉ là cách scale mô hình cho đẹp.

### 2.4. Foundation models cho DNA, long-context, và kiến trúc mới

Sau DNABERT, trọng tâm dịch chuyển khá rõ sang hai câu hỏi: `pretrain trên dữ liệu nào` và `xử lý ngữ cảnh dài bằng kiến trúc nào`.

- [HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution](https://arxiv.org/abs/2306.15794), *arXiv* (2023, preprint).
  - Paper này quan trọng vì nó đại diện cho hướng `long-context genomics`: xử lý chuỗi DNA rất dài ở độ phân giải nucleotide.
  - Dù là preprint, nó là mốc kỹ thuật đáng giữ trong survey vì đặt ra bài toán mà attention thuần túy xử lý khá tốn kém.

- [Nucleotide Transformer: building and evaluating robust foundation models for human genomics](https://www.nature.com/articles/s41592-024-02523-z), *Nature Methods* (2025; bản journal của công trình công bố cuối 2024).
  - Đây là một trong những foundation model DNA quan trọng nhất giai đoạn gần đây, nhấn mạnh transfer learning, low-data fine-tuning, và pretraining trên dữ liệu người cộng đa loài.
  - Paper này cũng hữu ích vì trình bày khá hệ thống việc xây `genomics foundation models`, không chỉ nêu một benchmark đơn lẻ.

- [Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling](https://proceedings.mlr.press/v235/schiff24a.html), *ICML / PMLR* (2024).
  - Caduceus đại diện cho hướng kiến trúc vượt ra ngoài Transformer thuần: tận dụng `bi-directionality`, `long-range modeling`, và `reverse-complement equivariance`.
  - Đây là ví dụ tốt cho việc inductive bias sinh học vẫn quan trọng, chứ không phải cứ scale model là đủ.

### 2.5. RNA sequence analysis

So với DNA và protein, RNA thường bị survey ngắn hơn, nhưng hiện đã đủ lớn để xem là một nhánh riêng.

- [RNA sequence analysis landscape: A comprehensive review of task types, databases, datasets, word embedding methods, and language models](https://pubmed.ncbi.nlm.nih.gov/39897847/), *Heliyon* (2025).
  - Đây là review rất hữu ích nếu bạn muốn nhìn RNA như một landscape hoàn chỉnh thay vì chỉ nhặt vài mô hình lẻ.
  - Bài này có giá trị ở chỗ hệ thống hóa `task types`, `datasets`, `embedding methods`, và `language models`, qua đó cho thấy RNA sequence ML vẫn phân mảnh hơn DNA/protein.

## 3. Reading list đề xuất

Nếu muốn đọc nhanh nhưng vẫn nắm được tiến hóa của field, mình sẽ ưu tiên 11 bài sau:

1. [An introduction to deep learning on biological sequence data: examples and solutions](https://academic.oup.com/bioinformatics/article-abstract/33/22/3685/4092933), *Bioinformatics* (2017).
   - Review nhập môn tốt nhất để vào field nếu chưa quen biological sequences.

2. [Deep learning: new computational modelling techniques for genomics](https://pubmed.ncbi.nlm.nih.gov/30971806/), *Nature Reviews Genetics* (2019).
   - Review kinh điển cho genomics ML trước làn sóng foundation models.

3. [Language models for biological research: a primer](https://pubmed.ncbi.nlm.nih.gov/39122951/), *Nature Methods* (2024).
   - Primer mới, rất hợp để nối NLP-style language modeling với sinh học.

4. [Predicting the sequence specificities of DNA- and RNA-binding proteins by deep learning](https://pubmed.ncbi.nlm.nih.gov/26213851/), *Nature Biotechnology* (2015).
   - Paper mốc cho motif discovery và binding prediction từ sequence.

5. [Predicting effects of noncoding variants with deep learning-based sequence model](https://pubmed.ncbi.nlm.nih.gov/26301843/), *Nature Methods* (2015).
   - Paper bắt buộc đọc nếu quan tâm regulatory genomics và variant effect prediction.

6. [DanQ: a hybrid convolutional and recurrent deep neural network for quantifying the function of DNA sequences](https://pmc.ncbi.nlm.nih.gov/articles/PMC4914104/), *Nucleic Acids Research* (2016).
   - Đại diện cho thời kỳ `CNN + RNN` trước khi Transformer thống trị.

7. [DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome](https://pmc.ncbi.nlm.nih.gov/articles/PMC11025658/), *Bioinformatics* (2021).
   - Mốc chuyển từ task-specific genomics models sang DNA pretraining.

8. [Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences](https://pmc.ncbi.nlm.nih.gov/articles/PMC8053943/), *PNAS* (2021).
   - Paper nên đọc để hiểu vì sao protein language models tạo ra lực kéo rất lớn cho cả field.

9. [HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution](https://arxiv.org/abs/2306.15794), *arXiv* (2023).
   - Đại diện cho hướng long-context genomics; giữ trong list như một preprint mốc kỹ thuật.

10. [Nucleotide Transformer: building and evaluating robust foundation models for human genomics](https://www.nature.com/articles/s41592-024-02523-z), *Nature Methods* (2025).
    - Một trong những bài quan trọng nhất nếu bạn muốn xem DNA foundation models đã trưởng thành đến đâu.

11. [Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling](https://proceedings.mlr.press/v235/schiff24a.html), *ICML / PMLR* (2024).
    - Đọc để thấy hướng kiến trúc mới và sinh học cảm ứng (`reverse-complement equivariance`) được đưa vào model như thế nào.

Để cân bằng danh sách bằng một bài `review/benchmark` thiên về đánh giá hơn là giới thiệu model, nên thêm:

- [RNA sequence analysis landscape: A comprehensive review of task types, databases, datasets, word embedding methods, and language models](https://pmc.ncbi.nlm.nih.gov/articles/PMC11783440/), *Heliyon* (2025).
- [Benchmarking DNA foundation models for genomic and genetic tasks](https://www.nature.com/articles/s41467-025-65823-8), *Nature Communications* (2025).

## 4. Xu hướng và lỗ hổng nghiên cứu

### 4.1. Từ motif cục bộ sang biểu diễn tổng quát

Các paper sớm như `DeepBind`, `DeepSEA`, `DanQ` chủ yếu giải quyết các task rõ ràng bằng supervised learning. Từ `DNABERT` trở đi, mục tiêu đổi thành học một biểu diễn tổng quát của chuỗi rồi transfer sang nhiều task. Đây là cùng logic đã xảy ra ở NLP và protein ML.

### 4.2. Foundation models mạnh ở embedding và transfer, nhưng không đồng nghĩa với “giải xong bài toán sinh học”

Theo [Benchmarking DNA foundation models for genomic and genetic tasks](https://www.nature.com/articles/s41467-025-65823-8), các DNA foundation models hiện khá cạnh tranh ở nhiều bài sequence classification và pathogenic variant identification khi dùng zero-shot embeddings. Tuy nhiên, benchmark này cũng cho thấy chúng yếu hơn các mô hình chuyên biệt trong vài bài như `gene expression prediction` hay nhận diện causal QTL. Nói ngắn gọn: embedding tốt chưa chắc đồng nghĩa với mechanistic modeling tốt.

### 4.3. Benchmark vẫn chưa thật thống nhất

Ngay cả trong DNA alone, benchmark đã rất đa dạng về sequence length, species, pooling strategy, negative sampling, và downstream protocol. Khi mở sang `RNA` và `protein`, sự phân mảnh còn lớn hơn nữa. Review RNA năm 2025 cho thấy số lượng task, database, và representation choices quá nhiều, nên so sánh ngang giữa các mô hình vẫn khó.

### 4.4. Leakage theo similarity/homology split vẫn là điểm phải cảnh giác

Trong biological sequence ML, chia train/test ngẫu nhiên thường dễ làm kết quả lạc quan quá mức vì các sequence gần nhau về mặt tiến hóa hoặc motif có thể rơi vào cả hai phía. Điểm này được nhắc lại nhiều trong review/benchmark gần đây, và là một lý do khiến các con số SOTA giữa các paper khó so trực tiếp nếu protocol split khác nhau.

### 4.5. Zero-shot và interpretability vẫn chưa đủ vững

Primer năm 2024 và benchmark năm 2025 đều gợi ý rằng `zero-shot embeddings` hữu ích, nhưng mức độ ổn định tùy task. Ngoài ra, dù attention maps, saliency maps, motif attribution đã rất phổ biến, `interpretability` trong sequence biology vẫn chưa hoàn toàn đáng tin như một bằng chứng cơ chế. Nói cách khác, mô hình có thể highlight motif đúng mà vẫn chưa thật sự học đúng causal mechanism.

## 5. Kết luận ngắn

Nếu bạn hỏi “có bài báo ML nào cho `biological sequence analysis` không?”, câu trả lời là có rất nhiều, và đây là một nhánh đã trưởng thành rõ rệt. Trục tiến hóa lớn nhất của field là:

- từ `motif discovery` và `regulatory classification`,
- sang `variant effect prediction`,
- rồi đến `protein/DNA language models`,
- và hiện tại là `foundation models`, `long-context genomics`, cùng các benchmark zero-shot.

Nếu chỉ đọc ít mà vẫn đủ nắm field, mình sẽ ưu tiên theo thứ tự: `DeepBind -> DeepSEA -> DanQ -> DNABERT -> Rives/ESM -> Nucleotide Transformer -> Caduceus -> benchmark 2025`, rồi dùng RNA review 2025 để lấp phần còn thiếu ở nhánh RNA.
