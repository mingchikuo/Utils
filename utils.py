def unzip(zip_dir, unzip_dir):
    def gen_sorted_key(x):
        x = os.path.basename(x)
        _, doctor_id, upload_time = x.split('_')
        upload_time = upload_time.replace('T', '')
        upload_time = upload_time.replace('Z.zip', '')
        return upload_time

    zips = []
    for file in os.listdir(zip_dir):
        if not file.lower().endswith('.zip'):
            continue
        zips.append(os.path.join(zip_dir, file))
    zips = sorted(zips, reverse=True, key=gen_sorted_key)
    #print(zips)

    filter_date = datetime.datetime.now().strftime('%Y%m%d')
    for zip_ in zips:
        _, doctor_id, upload_time = os.path.basename(zip_).split('_')
        if filter_date == upload_time.split('T')[0]:
            print('Skip: {}'.format(zip_))
            continue
        output_dir = os.path.join(unzip_dir, doctor_id)
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        with zipfile.ZipFile(zip_, mode='r') as z:
            for file in z.infolist():
                z.extract(file, output_dir)
        print('Unpack zip file: {}'.format(zip_))