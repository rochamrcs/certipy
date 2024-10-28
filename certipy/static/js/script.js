document.addEventListener('DOMContentLoaded', function() {
            document.querySelector('.certificado-btn').addEventListener('click', async function() {
                const { jsPDF } = window.jspdf;
                const pdf = new jsPDF('l', 'mm', 'a4'); // 'l' para orientação paisagem
                
                // Seleciona todas as páginas do certificado
                const certificadoPages = document.querySelectorAll('.certificado-page');

                for (let i = 0; i < certificadoPages.length; i++) {
                    const page = certificadoPages[i];
                    // Captura cada página inteira (texto + imagem)
                    const canvas = await html2canvas(page, { scale: 2 });
                    const imgData = canvas.toDataURL('image/png');
                    const imgWidth = 297; // Largura A4 em mm
                    const imgHeight = (canvas.height * imgWidth) / canvas.width;

                    // Adiciona a imagem ao PDF
                    if (i > 0) pdf.addPage();
                    pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);
                }
                
                pdf.save('certificado.pdf');
            });
        });