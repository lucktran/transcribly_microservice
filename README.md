Receiving Data

In the microservice Flask application, the /transcribe endpoint receives a JSON payload with bucketName and source parameters from the front-end website.

Example Call:

@app.route('/transcribe', methods=['POST'])
def download_file():
    bucket_name = request.json.get('bucketName')
    source = request.json.get('source')

The source is the file name of the video to be transcribed and bucketName is the name of the Supabase storage bucket where the file is stored. The download_file function downloads the video file, transcribes it, generates captions, overlays the captions on the video, and uploads the captioned video and the transcriptions back to the Supabase storage.

Sending Data

Once the transcription and captioning processes are completed, the microservice uploads the transcribed and captioned video back to the Supabase storage. It zips the captioned video, the SRT file with the captions, and the text file with the transcription together, and uploads the zipped file to the Supabase storage.

Example Call:

with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    zip_file.write(output_filename)
    zip_file.write(srt_filename)
    zip_file.write(transcription_filename)

try:
    with open(zip_filename, 'rb') as f:
        supabase.storage.from_(bucket_name).upload(zip_filename, f)
except Exception as e:
    logging.error("Error uploading zip file to Supabase: %s", e)
    return 'Error uploading zip file to Supabase', 500

The uploaded zipped file can then be retrieved from the Supabase storage by the front-end user.

UML Diagram:
Transcribly Frontend > Transcribly Microservice: POST /transcribe {bucketName, source}
Transcribly Microservice > Supabase Database: Download video
Transcribly Microservice > Transcribly Microservice: Transcribe video
Transcribly Microservice > Transcribly Microservice: Generate captions
Transcribly Microservice > Transcribly Microservice: Overlay captions on video
Transcribly Microservice > Transcribly Microservice: Zip captioned video, SRT file, and transcriptions
Transcribly Microservice > Supabase Database: Upload zip file
