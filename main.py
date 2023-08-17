import speedtest


def main():
    download_speed = speedtest.Speedtest()
    print(f'Download Speed: {download_speed.download()/8000000:.2f}mb')

    upload_speed = speedtest.Speedtest()
    print(f'Upload Speed: {upload_speed.upload()/8000000:.2f}mb')


if __name__ == "__main__":
    main()
