if __name__ == "__main__":
    import os
    import sys

    package_path = os.path.join(os.getcwd(), "EMLMailReader")
    if package_path not in sys.path:
        sys.path.append(package_path)
        print(f"{package_path} added to sys.path collection successfully.")
    from EMLMailReader import MailReader
    from EMLMailReader import RxMailMessage

    reader: MailReader = MailReader(os.getcwd())
    EMLFileNames = list[str]()
    InputFolder = os.path.join(os.getcwd(), "Input")
    OutputFolder = os.path.join(os.getcwd(), "Output")
    for item in os.listdir(InputFolder):
        if os.path.isfile(os.path.join(InputFolder, item)) and item.lower().endswith(".eml"):
            EMLFileNames.append(os.path.join(InputFolder, item))
    for EMLFileName in EMLFileNames:
        message: RxMailMessage = reader.get_email(EMLFileName)
        if message is not None:
            file_name = os.path.basename(EMLFileName).replace(".eml", "")
            TargetOutputFolderForEmail = os.path.join(OutputFolder, file_name)
            if not os.path.exists(TargetOutputFolderForEmail):
                os.mkdir(TargetOutputFolderForEmail)
                print(f"Target Folder - {TargetOutputFolderForEmail} has been created successfully.")
            json_string = message.export_as_json()
            TargetJsonFilePath = os.path.join(TargetOutputFolderForEmail, f"{file_name}.json")
            with open(TargetJsonFilePath, "wt") as my_json_file:
                my_json_file.write(json_string)
            if os.path.exists(TargetJsonFilePath):
                print(f"JSON file - {TargetJsonFilePath} has been created successfully.")
            if message.Attachments.length() > 0:
                message.save_attachments(TargetOutputFolderForEmail)
        else:
            print(f"ERROR while processing {EMLFileName}:> There were some internal errors while processing the EML file.")
