# The Stealer - Windows Data Stealer

🚧 **Development Status:** Under Development  
⏳ **Time Invested:** Started on February 12, 2024, ended on February 25, 2024  
⏰ **Hours:** 56 hours  
👨‍💻 **Developer:** Akki  
📸 **Instagram:** [@akki_raj_._](https://www.instagram.com/its_just_me_akki/)



## Introduction to the Data Stealer Project

In the contemporary digital ecosystem, where data permeates every facet of our lives, ensuring its security and integrity is paramount. The Data Stealer project emerges as an educational initiative, meticulously crafted to explore and elucidate the complexities of data security, encryption, and privacy practices within computer systems.

### Purpose

The Data Stealer project serves as a comprehensive tool for dissecting and demonstrating the vulnerabilities inherent in digital systems. Developed for educational exploration, it offers insights into data extraction, encryption, and transmission, shedding light on potential security breaches and their ramifications.

## Functionalities

The Data Stealer project encompasses a wide array of functionalities, allowing for:

- **Data Extraction**: With the ability to extract various types of data from target systems, including:
  - System information
  - Chrome browser data (basic and comprehensive)
  - Chrome ID passwords
  - Chrome web data
  - Chrome history data
  - Edge browser data
  - File stealing by Directory searches

- **Encryption and Decryption**: Recognizing the critical importance of data security, the project incorporates robust encryption algorithms to safeguard harvested data. Moreover, it provides decryption mechanisms to illustrate the process of accessing encrypted data, emphasizing the importance of secure transmission.

- **Advanced Features**: Beyond mere data extraction, the project offers advanced functionalities such as:
  - Encrypting entire systems
  - Facilitating file transfers
  - Displaying messages to users
  - Executing file deletions

## /!\ Errors in Code

Errors currently encountered in The Stealer project that will be addressed in future updates:

### 1. /!\ No Passwords Displayed after Extraction

This issue arises during password decryption on our local machine due to differences in environment and DD-API between our computer and the victim's computer. The `win32crypt.CryptUnprotectData` function used for decrypting Chrome encryption keys on our computer fails due to these differences. Interestingly, the same action performed on the victim's computer does not encounter this error. To address this issue in the next update, we will:

1. Implement a function to decrypt passwords on the victim's computer.

2. Modify the data structure to directly store passwords, eliminating the need for encryption keys. Changes will be made in:

   - Edge Data Extractor Function Data Structure
   - Edge Data Configuration Function Data Structure
   - Chrome ID Password Extractor Function Data Structure
   - Chrome ID Password Configuration Function Data Structure
   - `row_virus.py` Modification

These updates aim to enhance decryption processes and improve compatibility across different computer systems.

### 2. /!\ Deletion Failure in `virus.py` after Extraction and Sending of Data

The error could be caused by the deletion code being called within `row_virus.py` without proper permissions to delete files, or due to the existence of code in `row_virus.py` after the deletion code. As a result, the deletion of files fails. This error has not been fully identified yet, but it will be addressed in the next update.

## Future Developments

As the Data Stealer project continues to evolve, there are several exciting developments that we plan to incorporate in future updates. These enhancements will further expand the capabilities of the project and ensure its relevance in the ever-changing landscape of cybersecurity:

- **Enhanced Stealth Mechanisms:** Future versions of the project will incorporate advanced techniques to evade detection by antivirus software and security measures, ensuring improved stealth and effectiveness.

- **Error Handling and Data Extraction:** We will implement robust error handling mechanisms to ensure smooth operation and data extraction under all circumstances, regardless of any encountered errors.

- **Expansion of Data Acquisition:** We aim to broaden the scope of data acquisition by adding new categories of sensitive information, including Windows passwords, critical system information such as DD-API, user data, password lists, CREDHIST, NTLM HASH, Master Key, ASA DIR, and more.

- **Comprehensive System Manipulation:** We will introduce features to decrypt entire computers or even render them inoperable, providing users with unprecedented control over targeted systems.

- **Installation of RATs and Backdoors:** Future updates will include capabilities for installing Remote Access Trojans (RATs) or backdoors through the assistance of the virus, enabling remote access and control over compromised systems.

- **Keylogger Installation:** We plan to integrate functionality for installing keyloggers, allowing for the capture of keystrokes and sensitive information entered by users.

- **Installation of Additional Software:** The project will facilitate the installation of additional software, such as Telegram, Minecraft, and banking applications, with their details stored in hash format for educational purposes.

- **Ongoing Improvement and Expansion:** The development of the Data Stealer project will continue indefinitely, with a commitment to ongoing improvement and expansion. We will strive to make it the best-in-class tool for educational purposes, continuously adding new features and capabilities to meet the evolving needs of cybersecurity education and exploration.

- **User Interface Enhancements**: There could be improvements to the user interface to enhance usability and accessibility, making it easier for users to interact with the project.

- **Additional Educational Resources**: The project may include supplementary documentation, tutorials, and resources to provide users with more comprehensive educational support.

Stay tuned for these exciting developments and more as we work tirelessly to make the Data Stealer project the ultimate tool for cybersecurity education and exploration.

## Teaching Purpose and Potential Dangers

The Data Stealer project serves as an educational tool to demonstrate how a malicious script can compromise the security of a victim's computer. It showcases the potential dangers of unauthorized data extraction and transmission, emphasizing the importance of robust security measures and ethical practices. While developed for educational purposes, it's essential to recognize the risks associated with such scripts and the potential legal and ethical implications of their usage.

**Disclaimer**: This project is intended for educational purposes only. While efforts have been made to ensure that the software operates in a safe and controlled environment, it's important to understand that any use of this software in a real-world context may have legal and ethical implications. The creators of this project disclaim any responsibility for any harm or misuse resulting from the use of this software.

## Components

The architecture of the Data Stealer project comprises three core components:

- **main.py**: Serving as the central orchestrator, this component is responsible for creating and modifying the virus, as well as decrypting and extracting data. It encompasses functionalities for collecting system data, encrypting harvested data, viewing extracted data, and generating the virus.

- **row_virus.py**: At the heart of the malicious intent, this component represents the actual virus, whose behavior is contingent upon user execution. Modification of main.py dictates the actions of row_virus.py, ensuring that it remains inert unless activated by the user.

- **setup.py**: Streamlining the deployment process, this component facilitates the setup of the project, enabling users to configure and initialize the code effectively, emphasizing ease of use and accessibility.

## Usage Instructions

To use the Data Stealer project, follow these steps:

1. **Clone the Repository**: Open your terminal, cmd, or Git Bash and use the following command to clone the project repository:
comand-> `git clone https://github.com/Akkiraj1234/the_stealer`

2. **Setup**: Navigate to the cloned directory and run *setup.py* to initialize the project:
comand-> i. `cd the_stealer` ii. `python setup.py`

3. **Usage**: After setup is complete, you can safely delete the cloned repository folder if it's no longer needed, except for `main.py`, which is essential for running the project.

4. **Running the Script**: Move `main.py` to any desired folder. You can execute `main.py` to utilize the Data Stealer project for various purposes, as detailed further in the script itself.

5. **Creating the Virus**: Follow the instructions provided within `main.py` to create and customize the virus. Once created, transfer the virus to the victim's computer for execution.

6. **Data Storage**: All data collected by `main.py` will be stored in the directory:  `C:\Users\Public\akki\the_stealer`

7. **Error Reporting**: If you encounter any errors during setup or usage, please inform us via our Instagram page [@akki_raj_._](https://www.instagram.com/its_just_me_akki/).

**All Essential Commands**:

1. `git clone https://github.com/Akkiraj1234/the_stealer`
2. `cd the_stealer`
3. `python setup.py`
4. `python main.py`

By following these instructions, you can effectively utilize the Data Stealer project for educational purposes and understand its functionalities.

## Conclusion

In summary, the Data Stealer project stands as a powerful educational tool, empowering users with insights into data security vulnerabilities and encryption practices. By fostering a deeper understanding of potential threats and promoting ethical usage, it equips users to navigate the digital landscape with vigilance and proficiency.
