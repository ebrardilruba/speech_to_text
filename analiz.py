import Levenshtein
import re
import nltk
from nltk.tokenize import sent_tokenize
from Bio import pairwise2


def get_analysis_data():
    # Burada analiz verilerinizi hesaplayın veya alın
    analysis_data = "Bu metin analiz.py dosyasından geldi."
    return analysis_data



nltk.download('punkt')

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            text = ' '.join(line.strip() for line in lines)
            return text
    except FileNotFoundError:
        print(f"Hata: '{file_path}' dosyasi bulunamadi.")
        return None
    except Exception as e:
        print(f"Dosya okunurken bir hata oluştu: {e}")
        return None

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# def print_diff(text1, text2):
#     alignments = pairwise2.align.globalxx(text1, text2)
#     if not alignments:
#         print("Hizalama bulunamadı.")
#         return [], []
#     aligned_text1, aligned_text2 = alignments[0][:2]
#     result1, result2 = [], []
#     for a, b in zip(aligned_text1, aligned_text2):
#         result1.append(a)
#         result2.append(b)

#     print("".join(result1))
#     print("".join(['|' if a == b else '-' for a, b in zip(result1, result2)]))
#     print("".join(result2))


#     return result1, result2


def print_diff(text1, text2):
    alignments = pairwise2.align.globalxx(text1, text2)
    if not alignments:
        print("Hizalama bulunamadı.")
        return "Hizalama bulunamadı."

    aligned_text1, aligned_text2 = alignments[0][:2]
    result1, result2 = [], []
    for a, b in zip(aligned_text1, aligned_text2):
        result1.append(a)
        result2.append(b)

    # Birleştirilmiş string'in oluşturulması
    result_text = "".join(result1) + "\n" + \
                  "".join(['|' if a == b else '-' for a, b in zip(result1, result2)]) + "\n" + \
                  "".join(result2)
    
    # Ekrana yazdırılması
    print(result_text)
    
    return result_text  # Tek bir string olarak sonuçların dönülmesi



def split_text_into_chunks(text, chunk_size):
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def compare_texts():
    try:

        file_path1 = r"C:\Users\ebrar\OneDrive\Masaüstü\orijinalmetin.txt"
        file_path2 = r"C:\Users\ebrar\OneDrive\Masaüstü\filtreli_metin.txt"
        chunk_size = 5
        raw_text1 = read_text_file(file_path1)
        raw_text2 = read_text_file(file_path2)
        
        if raw_text1 is None or raw_text2 is None:
            print("Metinler karşılaştırılamadı çünkü en az bir dosya okunamadı.")
            return

        chunks1 = split_text_into_chunks(raw_text1, chunk_size)
        chunks2 = split_text_into_chunks(raw_text2, chunk_size)

        max_length = max(len(chunks1), len(chunks2))
        chunks1.extend([''] * (max_length - len(chunks1)))
        chunks2.extend([''] * (max_length - len(chunks2)))
    

        overall_text1 = ''
        overall_text2 = ''
        combined_results = ""
        for chunk1, chunk2 in zip(chunks1, chunks2):
            try:
                text1 = preprocess_text(chunk1)
                text2 = preprocess_text(chunk2)

                overall_text1 += text1 + ' '
                overall_text2 += text2 + ' '

                similarity = Levenshtein.ratio(text1, text2) * 100
                print(f"\nBenzerlik Oranı: {similarity:.2f}%")
                
                combined_results += print_diff(text1, text2) 
            except:
                print("an erro occured")

        overall_similarity = Levenshtein.ratio(overall_text1.strip(), overall_text2.strip()) * 100
        
        print(f"\nTüm Metindeki Benzerlik Oranı: {overall_similarity:.2f}%")
        return combined_results
    except:
        print("An error occured")




# File paths
original_file_path = r"C:\Users\ebrar\OneDrive\Masaüstü\orijinalmetin.txt"
filtered_file_path = r"C:\Users\ebrar\OneDrive\Masaüstü\filtreli_metin.txt"

# Call the function and print the results
#compare_texts()
#compare_texts_by_sentences(original_file_path, filtered_file_path)