# import matplotlib
# import pandas as pd
#
# matplotlib.use('Agg')
#
# import matplotlib.pyplot as plt
# import numpy as np
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from annotated_text import annotated_text
from matplotlib import pyplot as plt


def timeline_chart(icds, title=""):
    # In case the above fails, e.g. because of missing internet connection
    # use the following lists as fallback.
    names = icds
    base = datetime.today()
    dates = [base - timedelta(days=x) for x in range(len(names))]
    # dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
    #          '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
    #          '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
    #          '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
    #          '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
    #          '2014-10-26', '2014-10-18', '2014-08-26']

    # Convert date strings (e.g. 2014-10-18) to datetime
    #dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

    # Choose some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates) / 6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    ax.set(title=title)

    ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
    ax.plot(dates, np.zeros_like(dates), "-o",
            color="k", markerfacecolor="w")  # Baseline and markers on it.

    # annotate lines
    for d, l, r in zip(dates, levels, names):
        ax.annotate(r, xy=(d, l),
                    xytext=(-3, np.sign(l) * 3), textcoords="offset points",
                    horizontalalignment="right",
                    verticalalignment="bottom" if l > 0 else "top")

    # format xaxis with 4 month intervals
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

    # remove y axis and spines
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    # ax.spines[["left", "top", "right"]].set_visible(False)

    ax.margins(y=0.1)
    plt.savefig("prueba.png")
    #plt.show()
    return fig

icds=["R50","K56"]
timeline_chart(icds)


def get_ejemplo_1():
    return ("HISTORY OF PRESENT ILLNESS\n"
            "The night of admission he developed a right arm fine tremor that increased in"
            " intensity over the next hour and he fell forward hitting his face on the ground and became unresponsive. "
            "At the time he was evaluated, he was nonverbal with right facial droop and questionable right arm weakness. "
            "Twenty minutes later the patient had a grand tonic clonic seizure in the transport vehicle the patient was "
            "intubated and brought to the trauma intensive care unit where he was started on dilantin and propofol. "
            "The patient had a notable chronic bilateral frontal  subdural hygromas and nasal bone fracture."
            "The patient was admitted to the trauma ctu for repair of the nasal bone fracture. maintained on a p o once "
            "daily dose of dilantin with stable vital signs and thereafter was transferred to the neurology service for "
            "further management and etiology of his new grand tonic clonic seizure. \n\n"
            "PAST MEDICAL HISTORY\n"
            "hypertension, insulin dependent diabetes mellitus, low grade prostate cancer  and  "
            "recurrent invasive melanoma"
            "MEDICATIONS PRIOR TO ADMISSION\n"
            "lisinopril, humulin, insulin, avandia, aspirin and tylenol\n\n"
            "HOSPITAL COURSE \n"
            "The patient was admitted to the neurology service after trauma he sustained for nasal bone fracture. "
            "The patient was transitioned from dilantin to keppra during the admission for seizure prophylaxis. The "
            "etiology of the patient s seizures were unresolved at the time of discharge as they could be due to bi "
            "lateral subdural hydroma collection or possible metastatic melanoma involving cerebrum. The patient had "
            "no more seizures during the admission and was placed back on his diabetes medication with oxybutynin and "
            "chloride as patient was having urinary difficulties in the two days prior to discharge the patient was also"
            " started on lisinopril and aspirin for cardiovascular and stroke prophylaxis. The patient s diet was "
            "advanced from liquids to full consistency without any difficulty the patient was seen by physical therapy "
            "and approved for discharge to home with home physical therapy services\n\n"
            "DISCHARGE STATUS \n"
            "Home with physical therapy\n\n"
            "DISCHARGE DIAGNOSIS \n"
            "Grand tonic clonic seizure of unknown etiology")

def get_ejemplo_1_marked():
    annotated_text(
        "HISTORY OF PRESENT ILLNESS \n"
        "The night of admission he developed a right arm fine tremor that increased in"
        " intensity over the next hour and he fell forward hitting his face on the ground and became unresponsive. "
        "At the time he was evaluated, he was nonverbal with right facial droop and ", ("questionable right arm weakness","","#a88b49"), ". "
        "Twenty minutes later the patient had a grand tonic clonic seizure in the transport vehicle the patient was "
        "intubated and brought to the trauma intensive care unit where he was started on dilantin and propofol. "
        "The patient had a", ("notable chronic bilateral frontal  subdural hygromas","","#a2f5a8"), "and",
        ("nasal bone fracture.","", "#cea2f5"),
        "The patient was admitted to the trauma ctu for repair of the ", ("nasal bone fracture","", "#cea2f5"), " maintained on a p o once "
        "daily dose of dilantin with stable vital signs and thereafter was transferred to the neurology service for "
        "further management and etiology of his new grand tonic clonic seizure.\n\n"
        "PAST MEDICAL HISTORY \n",
        ("hypertension","","#f3f5a2"), ", ",("insulin dependent diabetes mellitus","","#a2c6f5"), ", low grade ",("prostate cancer","","#99f0de"), "  and  "
        "",("recurrent invasive melanoma","","#f0999f"), "\n\n"
        "MEDICATIONS PRIOR TO ADMISSION \n"
        "lisinopril, humulin, insulin, avandia, aspirin and tylenol\n\n"
        "HOSPITAL COURSE \n"
        "The patient was admitted to the neurology service after trauma he sustained for ", ("nasal bone fracture","", "#cea2f5"), ". "
        "The patient was transitioned from dilantin to keppra during the admission for seizure prophylaxis. The "
        "etiology of the patient s seizures were unresolved at the time of discharge as they could be due to bi "
        "lateral subdural hydroma collection or possible metastatic melanoma involving cerebrum. The patient had "
        "no more seizures during the admission and was placed back on his ",("diabetes","","#a2c6f5"), " medication with oxybutynin and "
        "chloride as patient was having urinary difficulties in the two days prior to discharge the patient was also"
        " started on lisinopril and aspirin for cardiovascular and stroke prophylaxis. The patient s diet was "
        "advanced from liquids to full consistency without any difficulty the patient was seen by physical therapy "
        "and approved for discharge to home with home physical therapy services\n\n"
        "DISCHARGE STATUS\n"
        "Home with physical therapy\n\n"
        "DISCHARGE DIAGNOSIS\n"
        "Grand tonic clonic seizure of unknown etiology"
    )


def get_ejemplo_1_marked_ICD():
    annotated_text(

        (" 780.39", "", "#fcc23a"), ":Convulsions"
    )

    annotated_text(

        (" 852.20", "", "#a2f5a8"), "Subdural hemorrhage following injury without mention of open intracranial wound, "
                                "unspecified state of consciousness"
    )

    annotated_text(

        (" 802.0", "", "#cea2f5"), ":Closed fracture of nasal bones"
    )

    annotated_text(

        (" 250.00", "", "#a2c6f5"), ":Diabetes mellitus without mention of complication, type II or unspecified type,"
                                " not stated as uncontrolled"
    )

    annotated_text(

        (" 401.9", "", "#f3f5a2"), ":Unspecified essential hypertension"
    )

    annotated_text(

        (" 185", "", "#99f0de"), ":Malignant neoplasm of prostate"
    )

    annotated_text(

        (" V10.82", "", "#f0999f"), ":Personal history of malignant melanoma of skin"
    )

    annotated_text(

        (" 728.89", "", "#a88b49"), ":Other disorders of muscle, ligament, and fascia"
    )


def get_ejemplo_1_cronology():
    return ["401.9","250.00","V10.82","185", "780.39","728.89","852.20","802.0"]

def get_ejemplo_1_future():
    lista_icd = ["348.4", "172.4", "191","438.0"]
    lista_definiciones = ["Brain Hernia", "Billable Malignant melanoma of skin of scalp and neck",
                          "Malignant neoplasm of brain", "Late effects of cerebrovascular disease, cognitive deficits" ]
    lista_confianza = ["70%", "62%", "57%", "51%"]

    df_futuro = pd.DataFrame(list(zip(lista_icd, lista_definiciones, lista_confianza)),
                             columns=["ICD", "Definition", "Confidence"])

    return df_futuro