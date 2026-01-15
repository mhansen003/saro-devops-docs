$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open('C:\Users\Mark Hansen\Desktop\saro\transcripts\Conditions Portal offsite_DAY1.docx')
$doc.Content.Text | Out-File -FilePath 'C:\Users\Mark Hansen\Desktop\saro\transcripts\temp_part1.txt' -Encoding UTF8
$doc.Close()
$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null

$word2 = New-Object -ComObject Word.Application
$word2.Visible = $false
$doc2 = $word2.Documents.Open('C:\Users\Mark Hansen\Desktop\saro\transcripts\Conditions Portal offsite_Day1_Part2.docx')
$doc2.Content.Text | Out-File -FilePath 'C:\Users\Mark Hansen\Desktop\saro\transcripts\temp_part2.txt' -Encoding UTF8
$doc2.Close()
$word2.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word2) | Out-Null
