import psycopg2
from task import Task

# Function to save tasks to PostgreSQL database
def save_tasks_to_db(task_manager):
    connection = connect_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                for task in task_manager.tasks:
                    query = """
                    INSERT INTO app.task (description, is_completed)
                    VALUES (%s, %s);
                    """
                    cursor.execute(query, (task.description, task.completed))
                connection.commit()
            print("Tasks saved to PostgreSQL.")
        except Exception as e:
            print(f"Error saving tasks to database: {e}")
        finally:
            connection.close()

# Function to load tasks from PostgreSQL database
def load_tasks_from_db(task_manager):
    connection = connect_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT description, is_completed FROM app.task")
                rows = cursor.fetchall()

                for row in rows:
                    task = Task(row[0])  # row[0] contains the description
                    if row[1]:  # row[1] contains is_completed
                        task.mark_done()
                    task_manager.add_task(task) #uneccesry to check again?
            print("Tasks loaded from PostgreSQL.")
        except Exception as e:
            print(f"Error loading tasks from database: {e}")
        finally:
            connection.close()

# Function to connect to the PostgreSQL database
def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="senavirat",
            password="senavirat"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
