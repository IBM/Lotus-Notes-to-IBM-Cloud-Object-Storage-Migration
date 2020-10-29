<p align="center">
  <h3 align="center">Lotus Notes to IBM Cloud Object Storage Migration</h3>

  <p align="center">
    This open source utility can migrate Lotus Notes Database(NSF) attachments to IBM Cloud Object Storage
    <br />
    <a href="https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration">Scope</a>
    ·
    <a href="https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration/issues">Report Bug</a>
    ·
    <a href="https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration/issues">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

We all know that IBM is planning to discontinue with Lotus Notes very soon. There are many applications which runs on Lotus Notes and we must either sunset or migrate those applications to some other platform.
For any migration project, the most critical question is – <b>“How you manage your existing Lotus Notes data?”</b>.<br /><br /> 
Existing Lotus Notes applications can have very important and confidential information which you may require to migrate to new environment for storage, reference, compliance or audit purpose. Unfortunately, there are very less options available to migrate Lotus Notes data to Cloudant or MongoDB or IBM Cloud Object Storage. There are some 3rd party tools, but it’s not secure and there is a risk exposing or compromising confidential data. We need a solution which is secure, scalable, easier to understand and implement. And for that purpose, I have developed solutions which can help team to migrate data from Lotus Notes to other databases on Cloud.

<b>IBM Cloud Object Storage</b> is the most suitable choice to store attachments. IBM Cloud® Object Storage makes it possible to store practically limitless amounts of data, simply and cost effectively. It is commonly used for data archiving and backup; for web and mobile applications; and as scalable, persistent storage for analytics. Flexible storage class tiers with a policy-based archive let you effectively manage costs while meeting data access needs. The integrated IBM Aspera® high-speed data transfer option makes it easy to transfer data to and from IBM Cloud Object Storage. Query-in-place functionality allows you to run analytics directly on your data.
I have developed this solution to migrate attachments from Lotus Notes database to IBM Cloud Object Storage. This solution offers several benefits,

1.	It’s easy to implement and it can be used with any IBM Notes database.
2.	It’s based-on HTTP and REST, so it’s fast and secure.
3.	Its written in Python which has excellent set of libraries to work with Data (Data Cleaning, Data Processing etc).
4.	You can migrate any number of attachments of different file types (jpg, pdf, xlxs, docx, pptx, wmv etc).
5.	There is no limitation on the attachment size. 
6.	Most importantly, once you are out of IBM Notes it will give you lot of options and opportunities to scale your application using modern tools. You can implement DevOps, TDD, AI and many others (Opportunities are endless).

### Built With

* [Python](https://www.python.org/downloads/)
* [Domino Access Service API](https://ds_infolib.hcltechsw.com/ldd/ddwiki.nsf/xpAPIViewer.xsp?lookupName=IBM+Domino+Access+Services+9.0.1#action=openDocument&content=catcontent&ct=api)
* [IBM Cloud Object Storage](https://www.ibm.com/cloud/object-storage)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need to install following Python packages
* pip
```sh
pip install ibm-boto3
pip install requests
```
You need to configure Domino Access Service API on your Domino server and database. Here are the instruction to setup and enable that, <br />
[Instructions to setup and enable Domino Access Service API][documentation-file]
### Installation

1. Clone the repo
```sh
git clone https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration.git
```
2. Install Python packages
```sh
pip install
```



<!-- USAGE EXAMPLES -->
## Usage

please refer to the [Documentation][documentation-file]



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

This code pattern is licensed under the Apache Software License, Version 2.  Separate third party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1 (DCO)](https://developercertificate.org/) and the [Apache Software License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache Software License (ASL) FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)



<!-- CONTACT -->
## Contact

Kirti Jha - kirtijha@in.ibm.com

Project Link: [https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration](https://github.com/IBM/Lotus-Notes-to-IBM-Cloud-Object-Migration)







<!-- MARKDOWN LINKS & IMAGES -->
[documentation-file]: documentation/IBM%20Notes%20to%20MongoDB%20Migration.docx