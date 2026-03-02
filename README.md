# mcafee-xpass 🛡️🔑

![GitHub release](https://img.shields.io/github/release/dawbar350z/mcafee-xpass.svg) ![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

**mcafee-xpass** is a lightweight Python tool designed to extract and decrypt administrator passwords from McAfee's `Sitelist.xml` configuration files. This tool decodes base64-encoded, XOR-obfuscated, and 3DES-encrypted password fields using a known static key and decryption scheme. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Encryption Methods](#supported-encryption-methods)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Release Information](#release-information)

## Features

- **Lightweight**: Minimal dependencies make it easy to use and integrate.
- **Versatile**: Supports multiple encryption and obfuscation methods.
- **User-Friendly**: Simple command-line interface for easy interaction.
- **Secure**: Focused on cybersecurity practices, ensuring safe handling of sensitive data.

## Installation

To install **mcafee-xpass**, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/dawbar350z/mcafee-xpass.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mcafee-xpass
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use **mcafee-xpass**, run the following command in your terminal:

```bash
python mcafee_xpass.py <path_to_Sitelist.xml>
```

Replace `<path_to_Sitelist.xml>` with the actual path to your `Sitelist.xml` file. The tool will extract and decrypt the administrator passwords and display them in the terminal.

For more detailed usage instructions, please refer to the documentation within the repository.

## Supported Encryption Methods

**mcafee-xpass** supports the following encryption methods:

- **Base64 Encoding**: Decodes base64-encoded password fields.
- **XOR Obfuscation**: Decrypts passwords that have been obfuscated using XOR.
- **3DES Encryption**: Utilizes a known static key to decrypt 3DES-encrypted passwords.

These methods ensure that you can access the necessary credentials for your cybersecurity tasks.

## Contributing

We welcome contributions to **mcafee-xpass**. If you would like to help improve the tool, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Submit a pull request for review.

Your contributions help enhance the tool and make it more useful for the community.

## License

**mcafee-xpass** is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For questions or feedback, feel free to reach out:

- **Email**: your-email@example.com
- **GitHub**: [dawbar350z](https://github.com/dawbar350z)

## Release Information

To download the latest release of **mcafee-xpass**, visit the [Releases](https://github.com/dawbar350z/mcafee-xpass/releases) section. Download the appropriate file and execute it to start using the tool.

![Releases](https://img.shields.io/badge/Download%20Latest%20Release-Here-brightgreen.svg)

## Additional Resources

- [McAfee Documentation](https://www.mcafee.com/enterprise/en-us/security-awareness/understanding-mcafee-sitelist-xml.html)
- [Python Official Documentation](https://docs.python.org/3/)
- [Cybersecurity Best Practices](https://www.cisa.gov/publications-library)

## Acknowledgments

- Thanks to the contributors who have helped improve this project.
- Special thanks to the cybersecurity community for their support and guidance.

---

**mcafee-xpass** aims to be a reliable tool for cybersecurity professionals and enthusiasts alike. With its straightforward design and powerful features, it simplifies the process of extracting and decrypting sensitive information from McAfee's configuration files.