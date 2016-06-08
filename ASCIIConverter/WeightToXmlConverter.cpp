#include "WeightToXmlConverter.h"

//============================================================================

WeightToXmlConverter::WeightToXmlConverter()
{
    this->LoadASCII();
    this->SaveXml();
}

//============================================================================

void WeightToXmlConverter::LoadASCII()
{
    std::string folder("/var/clus/usera/sg568/Whizard_v1-97/WhizardResults/vbswwww/1.4TeV/Weights/Alpha4_-0.02533_Alpha5_-0.02533");

    for (unsigned int i = 1; i < 101; i++)
    {
        std::string fileName(folder);
        fileName += "/whizard.";
        fileName += this->FileNumberToString(i);
        fileName += ".evt";

        ifstream file;
        file.open (fileName.c_str());

        if (!file.is_open()) return;

        std::string eventNumber;
        std::string weight;
        float alpha4 = -0.02533;
        float alpha5 = -0.02533;

        while (file >> eventNumber >> weight)
        {
            WeightToXmlConverter::Event *pEvent = new WeightToXmlConverter::Event();
            pEvent->SetAlpha4(alpha4);
            pEvent->SetAlpha5(alpha5);
            pEvent->SetEventNumber(atoi(eventNumber.c_str()));
            pEvent->SetWeight(atof(weight.c_str()));
            m_Events.push_back(pEvent); 
            std::cout << "For event number : " << eventNumber << ", the weight is " << weight << std::endl;
        }
    }
    return;
}

//============================================================================

void WeightToXmlConverter::SaveXml()
{
    TiXmlDocument tiXmlDocument;

    for (EventVector::iterator iter = m_Events.begin(); iter != m_Events.end(); iter++)
    {
        WeightToXmlConverter::Event *pEvent(*iter);

        TiXmlElement* pTiXmlElement = new TiXmlElement("Event");
        tiXmlDocument.LinkEndChild(pTiXmlElement);

        pTiXmlElement->SetAttribute("Event number", pEvent->GetEventNumber());
        pTiXmlElement->SetDoubleAttribute("Alpha Four", pEvent->GetAlpha4());
        pTiXmlElement->SetDoubleAttribute("Alpha Five", pEvent->GetAlpha5());
        pTiXmlElement->SetDoubleAttribute("Ratio of Integrands", pEvent->GetWeight());
    }

    bool success = tiXmlDocument.SaveFile("test_save.xml");

    tiXmlDocument.Clear();
}

//============================================================================

template <class T>
std::string WeightToXmlConverter::FileNumberToString(T Number)
{
    std::ostringstream ss;
    ss << setfill('0') << setw(3) << Number;
    return ss.str();
}

//============================================================================

int main(int argc, char* argv[])
{
    WeightToXmlConverter *pWeightToXmlConverter = new WeightToXmlConverter();
    return 0;
}
