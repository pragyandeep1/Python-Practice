from flask import Flask, request, jsonify, send_file
import csv
import json


class CSVConverter:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/upload', 'upload_file', self.upload_file, methods=['POST'])
        self.app.add_url_rule('/convert', 'convert_to_json', self.convert_to_json, methods=['GET'])
        self.app.add_url_rule('/download', 'download_file', self.download_file, methods=['GET'])

    def upload_file(self):
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            filename = file.filename
            file.save(filename)
            return jsonify({'message': 'File uploaded successfully', 'filename': filename})

    def convert_to_json(self):
        csv_filename = request.args.get('filename')
        if not csv_filename:
            return jsonify({'error': 'No CSV file specified'})

        json_filename = csv_filename.split('.')[0] + '.json'

        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return jsonify({'message': 'CSV file converted to JSON', 'filename': json_filename})

    def download_file(self):
        json_filename = request.args.get('filename')
        if not json_filename:
            return jsonify({'error': 'No JSON file specified'})

        return send_file(json_filename, as_attachment=True)


if __name__ == '__main__':
    converter = CSVConverter()
    converter.app.run(debug=True)
