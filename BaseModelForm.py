from pydantic import BaseModel


class AppForm(BaseModel):
    personalInfoName: str
    personalInfoLastName: str
    personalInfoSecondLastName: str
    personalInfoGender: str
    personalInfoSpeakEnglish: str
    personalInfoPhoto: str
    personalInfoBday: str
    personalInfoEmail: str
    personalInfoPhone: str
    personalInfoPhone2: str
    personalInfoCity: str
    personalInfoSuburban: str
    personalInfoStreet: str
    personalInfoCP: str

    fatherInfoName: str
    fatherInfoLastName: str
    fatherInfoSecondLastName: str
    fatherInfoSecondLastJob: str
    fatherInfoSecondFormalIncome: str
    fatherInfoSecondInformalIncome: str

    motherInfoName: str
    motherInfoLastName: str
    motherInfoSecondLastName: str
    motherInfoSecondLastJob: str
    motherInfoSecondFormalIncome: str
    motherInfoSecondInformalIncome: str

    economicStatusNumOfPeopleLivingAtHome: str
    economicStatusNumOfMembersFamily: str
    economicStatusHasOwnHouse: str
    economicStatusHasCar: str
    economicStatusHasBankAccount: str
    economicStatusHasInternet: str
    economicStatusHasJob: str
    economicStatusTimeLivingCabo: str

    academicBackgroundSecondarySchoolName: str
    academicBackgroundSecondarySchoolGrades: str
    academicBackgroundSecondarySchoolYears: str
    academicBackgroundSecondarySchoolAddress: str
    academicBackgroundHighySchoolName: str
    academicBackgroundHighySchoolGrades: str
    academicBackgroundHighySchoolYears: str
    academicBackgroundHighySchoolAddress: str

    extracurricularActivities: dict
    extracurricularAcknowledgements: dict
    signAccept: str
    signAcceptPublicImage: str
