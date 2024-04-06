# Rhythmic Ranker: Gymnastics Scoring Solution

## Overview

Rythmic Ranker is a cutting-edge solution designed to revolutionize the scoring process in rhythmic gymnastics competitions. Leveraging advanced technology, our solution aims to enhance accuracy, fairness, and efficiency in evaluating gymnastic performances. By integrating real-time data acquisition, artificial intelligence analysis, and intuitive presentation modules, Rhythmic Ranker provides judges with comprehensive insights, facilitating informed scoring decisions.

## Goal

The primary goal of Rhythmic Ranker is to address the inherent challenges and limitations associated with traditional scoring methods in rhythmic gymnastics. These challenges often stem from subjective interpretations, human error, and inefficiencies in data processing. Rhythmic Ranker seeks to overcome these obstacles by introducing a data-driven approach that ensures objective assessment based on measurable criteria.

## Solution Components

Rhythmic Ranker comprises three core components:

1. **Data Acquisition Interface:** Responsible for receiving continuous data streams from gymnastic performance capture systems via an API. These metrics are then stored in a dedicated time based database to facilitate seamless data management and scalability.

2. **Intelligent Analysis Module:** Utilizes advanced algorithms to analyze data stored in the time based database. This module determines the executed figure, conducts conformity checks against predefined scoring criteria, and ensures accurate and objective evaluation.

3. **Presentation Module:** Presents the estimated figure and conformity assessment derived from the intelligent analysis module in a user-friendly interface. This interface provides judges with clear, comprehensive, and real-time insights into gymnastic performances, streamlining the scoring process.

## Key Features

- Real-time data acquisition and analysis.
- Objective evaluation based on predefined scoring criteria.
- User-friendly interface for judges, facilitating informed scoring decisions.
- Scalable architecture, adaptable to varying competition requirements.
- Enhanced accuracy and fairness in scoring gymnastic performances.

## Legal Considerations

Rhythmic Ranker recognizes the importance of data security and legal compliance. To address these concerns, the solution incorporates robust security measures to safeguard data integrity and confidentiality during competitions. Additionally, clear guidelines are established for the external usage and exploitation of the solution to ensure compliance with relevant laws and regulations. Please refer to [LICENCE.md](./LICENCE.md).

## Getting Started

This repository contains the code and all electronic documentation necessary to recreate the Rhythmic Ranker project. To get started, please refer to the installation and usage instructions provided in the documentation. For any inquiries or support, feel free to contact our team.

## Open Innovation

Rhythmic Ranker is committed to open innovation, fostering collaboration and knowledge-sharing within the gymnastics community. We encourage contributions, feedback, and ideas from all stakeholders to continually improve and expand the capabilities of our solution (but please respect the rules given in [CONTRIBUTING.md](./CONTRIBUTING.md)).

**Why Open Innovation:**

This project has the potential to be modified for use in other sports. Our goal is to democratize assisted training/scoring technologies and ensure the continuity of the project as it is ambitious and long-term. To achieve this, we are offering the project to open source communities on Github to ensure its longevity.

**Elements put in place to make it an open project:**

- The entire codebase is available on Github and open to all
- The project is licensed under MIT to protect the project
- The project is framed by a contributor charter aimed at organizing the management of contributions (only submit functional code, document contributions, all communications related to the project must be public, etc.)
- All code and documentation is written in English to facilitate contribution and transmission of the project to anyone who wants it
- The code is documented according to best practices and open source development conventions (definition of necessary tools and versions, detailed explanations of the code, development by semi-independent bricks, automated work environment, etc.)
- A detailed presentation of the project is provided to attract potential contributors

**NOTE:** As the project still belongs to us, external contributions have been prohibited for the moment!

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/tristanqtn/Rhythmic-Ranker
   ```

   ```bash
   cd Rhythmic-Ranker
   ```

2. Depending on the components you want to install, follow the instructions in the respective directories:
   - [Software](./software/): this part of the solution is the whole system running on the jury's computer. This app opens a port to allow the connected object to connect to acquisition system and then handles all data sent by the object.
   - [Design](./design/README.md): find all 3D models and conception documents related to this project.
   - [Electronics](./electronics/README.md): this part of the solution is the connected object that will be used to acquire data from the gymnast's performance. It is composed of an Raspberry Pico W and an all sensors.
