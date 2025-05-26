# PC Screen Time Tracker

A real-time application usage tracking system that monitors and analyzes usage patterns of active windows on Windows computers. This Python-based tool provides comprehensive insights into computer usage habits with automatic data logging and persistence.

## Features

- **Real-time Window Monitoring**: Continuously tracks the currently active application window
- **Usage Analytics**: Records application usage duration, frequency, and switching patterns
- **Hierarchical Classification**: Categorizes applications into main and sub-applications for granular analysis
- **SQLite Database Integration**: Persistent data storage with automatic daily record management
- **Timestamp Tracking**: Logs first and last active timestamps for each application
- **JSON Export**: Real-time data export in JSON format for further analysis
- **Memory-Efficient**: Optimized to run continuously without significant CPU overhead

## Architecture

### Core Components

1. **Window Detection Module**: Uses Windows API (`win32gui`) to detect active windows
2. **Data Processing Engine**: Analyzes and categorizes application data
3. **Database Manager**: Handles SQLite operations and data persistence
4. **Analytics Engine**: Calculates usage statistics and generates insights

### Data Structure

The application tracks:
- **Window Title**: Full application window title
- **Main Application**: Primary application identifier
- **Sub Application**: Secondary classification for detailed analysis
- **Duration Metrics**: Total usage time per window and application category
- **Session Data**: First and last active timestamps
- **Usage Frequency**: Number of times each application was opened

## Installation

### Prerequisites

- Python 3.7 or higher
- Windows operating system
- Administrator privileges (recommended for full window access)

### Dependencies

Install required packages:

```bash
pip install pywin32 pynput
```

**Built-in modules used:**
- `sqlite3`
- `time`
- `datetime`
- `pprint`
- `json`

### Setup

1. Clone the repository:
```bash
git clone https://github.com/destinyN1/PC-screen-time-tracker.git
cd PC-screen-time-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Usage

### Starting the Tracker

```bash
python main.py
```

The application will:
1. Initialize the SQLite database (`screentime.db`)
2. Begin monitoring active windows
3. Display real-time usage statistics in the console
4. Automatically save data to the database

### Database Schema

The SQLite database contains a `screentime` table with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| `current_app` | TEXT | Full window title |
| `main_app` | TEXT | Primary application identifier |
| `sub_app` | TEXT | Secondary application identifier |
| `total_duration_window` | INTEGER | Total time spent in specific window |
| `Durmain` | INTEGER | Total time for main application |
| `Dursub` | INTEGER | Total time for sub application |
| `first_active` | TEXT | First recorded activity timestamp |
| `last_active` | TEXT | Most recent activity timestamp |
| `times_opened` | INTEGER | Application launch frequency |

### Data Analysis

The application provides several analysis features:

- **Hierarchical Usage Tracking**: Distinguishes between main applications and their sub-components
- **Session Management**: Tracks individual usage sessions with start/end times
- **Frequency Analysis**: Monitors how often applications are accessed
- **Daily Data Segregation**: Automatically creates new records for each day

## Configuration

### Customization Options

- **Polling Interval**: Modify the `time.sleep(1)` value in the main loop to adjust monitoring frequency
- **Database Location**: Change the database file path in `DataBase.py`
- **Application Classification**: Customize the string parsing logic in `FormatData()` function

### Performance Tuning

- **CPU Usage**: Increase sleep intervals for lower CPU usage
- **Memory Management**: The application uses efficient data structures to minimize memory footprint
- **Database Optimization**: SQLite provides efficient querying and storage for usage data

## File Structure

```
PC-screen-time-tracker/
├── main.py              # Main application logic and window monitoring
├── DataBase.py          # Database operations and SQLite management
├── screentime.db        # SQLite database (created automatically)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Technical Details

### Window Detection Algorithm

The application uses the Windows API to:
1. Detect the currently active window using `GetForegroundWindow()`
2. Extract window title using `GetWindowText()`
3. Parse application names from window titles
4. Track application switching events

### Data Processing Logic

- **Application Parsing**: Splits window titles using delimiter patterns to extract main and sub-applications
- **Duration Calculation**: Uses time-based calculations to track usage periods
- **State Management**: Maintains dictionaries for different tracking metrics
- **Database Synchronization**: Ensures data consistency between memory and persistent storage

### Error Handling

- **Window Title Encoding**: Handles non-ASCII characters in window titles
- **Database Exceptions**: Robust error handling for SQLite operations
- **Application Crashes**: Graceful handling of monitored application failures

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This application monitors computer usage for personal analytics purposes. Ensure compliance with local privacy laws and obtain necessary permissions before using in shared or corporate environments.

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository or contact the maintainer.

---

**Author**: Destiny Newman  
**GitHub**: [@DestinyN1](https://github.com/DestinyN1)  
**Project Link**: [PC Screen Time Tracker](https://github.com/destinyN1/PC-screen-time-tracker)# PC Screen Time Tracker

A real-time application usage tracking system that monitors and analyzes usage patterns of active windows on Windows computers. This Python-based tool provides comprehensive insights into computer usage habits with automatic data logging and persistence.

## Features

- **Real-time Window Monitoring**: Continuously tracks the currently active application window
- **Usage Analytics**: Records application usage duration, frequency, and switching patterns
- **Hierarchical Classification**: Categorizes applications into main and sub-applications for granular analysis
- **SQLite Database Integration**: Persistent data storage with automatic daily record management
- **Timestamp Tracking**: Logs first and last active timestamps for each application
- **JSON Export**: Real-time data export in JSON format for further analysis
- **Memory-Efficient**: Optimized to run continuously without significant CPU overhead

## Architecture

### Core Components

1. **Window Detection Module**: Uses Windows API (`win32gui`) to detect active windows
2. **Data Processing Engine**: Analyzes and categorizes application data
3. **Database Manager**: Handles SQLite operations and data persistence
4. **Analytics Engine**: Calculates usage statistics and generates insights

### Data Structure

The application tracks:
- **Window Title**: Full application window title
- **Main Application**: Primary application identifier
- **Sub Application**: Secondary classification for detailed analysis
- **Duration Metrics**: Total usage time per window and application category
- **Session Data**: First and last active timestamps
- **Usage Frequency**: Number of times each application was opened

## Installation

### Prerequisites

- Python 3.7 or higher
- Windows operating system
- Administrator privileges (recommended for full window access)

### Dependencies

Install required packages:

```bash
pip install pywin32 pynput
```

**Built-in modules used:**
- `sqlite3`
- `time`
- `datetime`
- `pprint`
- `json`

### Setup

1. Clone the repository:
```bash
git clone https://github.com/destinyN1/PC-screen-time-tracker.git
cd PC-screen-time-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Usage

### Starting the Tracker

```bash
python main.py
```

The application will:
1. Initialize the SQLite database (`screentime.db`)
2. Begin monitoring active windows
3. Display real-time usage statistics in the console
4. Automatically save data to the database

### Database Schema

The SQLite database contains a `screentime` table with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| `current_app` | TEXT | Full window title |
| `main_app` | TEXT | Primary application identifier |
| `sub_app` | TEXT | Secondary application identifier |
| `total_duration_window` | INTEGER | Total time spent in specific window |
| `Durmain` | INTEGER | Total time for main application |
| `Dursub` | INTEGER | Total time for sub application |
| `first_active` | TEXT | First recorded activity timestamp |
| `last_active` | TEXT | Most recent activity timestamp |
| `times_opened` | INTEGER | Application launch frequency |

### Data Analysis

The application provides several analysis features:

- **Hierarchical Usage Tracking**: Distinguishes between main applications and their sub-components
- **Session Management**: Tracks individual usage sessions with start/end times
- **Frequency Analysis**: Monitors how often applications are accessed
- **Daily Data Segregation**: Automatically creates new records for each day

## Configuration

### Customization Options

- **Polling Interval**: Modify the `time.sleep(1)` value in the main loop to adjust monitoring frequency
- **Database Location**: Change the database file path in `DataBase.py`
- **Application Classification**: Customize the string parsing logic in `FormatData()` function

### Performance Tuning

- **CPU Usage**: Increase sleep intervals for lower CPU usage
- **Memory Management**: The application uses efficient data structures to minimize memory footprint
- **Database Optimization**: SQLite provides efficient querying and storage for usage data

## File Structure

```
PC-screen-time-tracker/
├── main.py              # Main application logic and window monitoring
├── DataBase.py          # Database operations and SQLite management
├── screentime.db        # SQLite database (created automatically)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Technical Details

### Window Detection Algorithm

The application uses the Windows API to:
1. Detect the currently active window using `GetForegroundWindow()`
2. Extract window title using `GetWindowText()`
3. Parse application names from window titles
4. Track application switching events

### Data Processing Logic

- **Application Parsing**: Splits window titles using delimiter patterns to extract main and sub-applications
- **Duration Calculation**: Uses time-based calculations to track usage periods
- **State Management**: Maintains dictionaries for different tracking metrics
- **Database Synchronization**: Ensures data consistency between memory and persistent storage

### Error Handling

- **Window Title Encoding**: Handles non-ASCII characters in window titles
- **Database Exceptions**: Robust error handling for SQLite operations
- **Application Crashes**: Graceful handling of monitored application failures

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This application monitors computer usage for personal analytics purposes. Ensure compliance with local privacy laws and obtain necessary permissions before using in shared or corporate environments.

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository or contact the maintainer.

---

**Author**: Destiny Newman  
**GitHub**: [@DestinyN1](https://github.com/DestinyN1)  
**Project Link**: [PC Screen Time Tracker](https://github.com/destinyN1/PC-screen-time-tracker)
