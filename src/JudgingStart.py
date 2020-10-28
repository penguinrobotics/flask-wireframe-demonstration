import FlaskServer as fs
import TeamStore as teams
import Configuration as config
import BackTasks as backtasks
import time

if __name__ == "__main__":
    print("Starting Common Init")
    print("Loading Config From File")
    config.load_config_from_file()
    print("Preparing Team Store")
    teams.load_from_file()
    teams.update_online()
    print("Starting Background Thread")
    backtasks.start_background_services()
    print("Starting Flask Thread")
    fs.start()

    print("Main Thread Exited from Flask")
    while backtasks.running:
        print("Idling while background thread exits")
        time.sleep(5)

    print("Background Task Terminated")
    print("Saving Synchronously")
    config.save_config_file()
    teams.save_to_file()
    print("Save completed, shutdown complete")
