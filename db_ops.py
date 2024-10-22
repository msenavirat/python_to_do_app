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

                
                tasks = [Task(description=row[0], completed=row[1]) for row in rows]

                task_manager.tasks.extend(tasks)  # Add all tasks at once
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
