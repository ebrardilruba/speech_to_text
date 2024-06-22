# import torch
# import torchaudio
# from torchaudio.transforms import Spectrogram, InverseSpectrogram

# def reduce_noise(spectrogram, threshold_db=-40): #gürültü azaltma fonksiyonu
#     # Spectrogram üzerinde bir gürültü azaltma işlemi yapiliyor
#     magnitude = spectrogram.abs() #mutlak deger alir
#     max_mag = magnitude.max() #maksimim genlik bulunur
#     mask = magnitude > (max_mag * (10**(threshold_db / 20))) #maske olusturuluyor ve esik deger ustundeki veriler korunuyor
#     return spectrogram * mask

# def process_file_cpu(filename, output_filename): #Ses dosyasını yukluyor
#     waveform, sample_rate = torchaudio.load(filename) #waveform(dalga formu) ve samplerate(ornekleme oranı) elde ediyor

#     # Spectrogram için transformer oluşturuluyor
#     spec_transform = Spectrogram(n_fft=1024, power=None)  # Kompleks çıktı için power=None
#     inv_spec_transform = InverseSpectrogram(n_fft=1024)

#     # Spectrogram sınıfı kullanılarak, ses sinyalini frekansa dönüştüren bir dönüşüm oluşturulur.
#     # n_fft=1024 parametresi, Fourier dönüşümü için kullanılan pencere büyüklüğünü belirtir. power=None seçeneği, 
#     #spektrogramın kompleks sayılar (hem genlik hem de faz bilgisi içeren) olarak hesaplanacağını belirtir. 
#     #InverseSpectrogram sınıfı ise bu işlemin tersini gerçekleştirir.

#     # STFT hesaplanıyor
#     spectrogram = spec_transform(waveform) #ses sinyali frekansa 

#     # Gürültü azaltılıyor
#     cleaned_spectrogram = reduce_noise(spectrogram) #gurultu temizlendi

#     # Zamana geri dönüştür
#     cleaned_waveform = inv_spec_transform(cleaned_spectrogram) #frekans ses sinyaline

#     # Dosyaya yaziliyor
#     torchaudio.save(output_filename, cleaned_waveform, sample_rate)

# # Kullanımı
# process_file_cpu('test3.wav', 'filtreli_test3_cpu.wav')