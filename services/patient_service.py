from config.database import SessionLocal
from config.models import Patient


def create_patient(data):
    db = SessionLocal()
    patient = Patient(**data.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    db.close()
    return patient


def get_patient(patient_id: int):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    db.close()
    return patient


def get_all_patients():
    db = SessionLocal()
    patients = db.query(Patient).all()
    db.close()
    return patients


def update_patient(patient_id: int, data):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        db.close()
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)
    db.close()
    return patient


def delete_patient(patient_id: int):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        db.close()
        return False

    db.delete(patient)
    db.commit()
    db.close()
    return True