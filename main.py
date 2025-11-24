from typing import List, Optional

from fastapi import FastAPI, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select

# --- Modelo de Datos ---
# SQLModel se encarga de ser tanto el modelo de la base de datos como el esquema de la API.
class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int
    course: str

# --- Conexión a la Base de Datos ---
# Usaremos una base de datos SQLite llamada "database.db" en el mismo directorio.
DATABASE_URL = "sqlite:///./database.db"

# El 'engine' es el punto de entrada a la base de datos.
# connect_args es necesario para SQLite para permitir múltiples hilos.
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Función para crear la tabla en la base de datos si no existe.
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# --- Lógica de la Aplicación FastAPI ---
app = FastAPI(
    title="API de Registro de Estudiantes",
    description="Un backend simple con FastAPI y SQLModel para gestionar estudiantes."
)

# --- Dependencia para obtener la sesión de la base de datos ---
# Esta función se ejecutará en cada petición que la necesite,
# asegurando que siempre haya una sesión de BD disponible y que se cierre al final.
def get_session():
    with Session(engine) as session:
        yield session

# --- Evento de Inicio ---
# Esto se ejecuta una sola vez cuando la aplicación FastAPI arranca.
# Es el lugar perfecto para crear la base de datos y las tablas.
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- Endpoints de la API ---

@app.post("/students/", response_model=Student, tags=["Students"])
def create_student(*, session: Session = Depends(get_session), student: Student):
    """
    Registra un nuevo estudiante en la base de datos.
    """
    # Añade la nueva instancia de estudiante a la sesión
    session.add(student)
    # Confirma la transacción para guardarla en la base de datos
    session.commit()
    # Refresca el objeto 'student' para obtener el ID asignado por la BD
    session.refresh(student)
    return student

@app.get("/students/", response_model=List[Student], tags=["Students"])
def read_students(*, session: Session = Depends(get_session)):
    """
    Devuelve una lista de todos los estudiantes registrados.
    """
    students = session.exec(select(Student)).all()
    return 
    
@app.get("/")
async def root():
    return {"message": "¡Bienvenido a la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro dea la API de Registro de Estudiantes!, Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro de Estudiantes! ,Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudianttudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes! Bienvenido a la API de Registro de Estudiantes!"}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o lista de dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
