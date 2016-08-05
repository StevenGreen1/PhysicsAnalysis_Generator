#include "WeightToXmlConverter.h"

//============================================================================

WeightToXmlConverter::WeightToXmlConverter(const std::string process, const std::string energy, const float alpha4, const float alpha5) :
    m_Process(process),
    m_Energy(energy),
    m_Alpha4(alpha4),
    m_Alpha5(alpha5)
{
    this->LoadASCII();
    this->SaveXml();
}

//============================================================================

void WeightToXmlConverter::LoadASCII()
{
    std::string folder("/usera/sg568/PhysicsAnalysis/Generator/WhizardResults/" + m_Process + "/" + m_Energy + "GeV/Weights/Alpha4_" + this->AlphasToString(m_Alpha4) + "_Alpha5_" + this->AlphasToString(m_Alpha5));
    std::cout << folder << std::endl;

    for (unsigned int i = 1; i <= 350; i++)
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

        while (file >> eventNumber >> weight)
        {
            WeightToXmlConverter::Event *pEvent = new WeightToXmlConverter::Event();
            pEvent->SetProcess(m_Process);
            pEvent->SetEnergy(m_Energy);
            pEvent->SetAlpha4(m_Alpha4);
            pEvent->SetAlpha5(m_Alpha5);
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

    TiXmlElement* pHeadTiXmlElement = new TiXmlElement("Process");
    tiXmlDocument.LinkEndChild(pHeadTiXmlElement);

    pHeadTiXmlElement->SetAttribute("Process", m_Process.c_str());
    pHeadTiXmlElement->SetAttribute("Energy", m_Energy.c_str());
    pHeadTiXmlElement->SetDoubleAttribute("Alpha_Four", m_Alpha4);
    pHeadTiXmlElement->SetDoubleAttribute("Alpha_Five", m_Alpha4);

    for (EventVector::iterator iter = m_Events.begin(); iter != m_Events.end(); iter++)
    {
        WeightToXmlConverter::Event *pEvent(*iter);
        TiXmlElement* pTiXmlElement = new TiXmlElement("Event");
        pTiXmlElement->SetAttribute("Event_Number", pEvent->GetEventNumber());
        pTiXmlElement->SetDoubleAttribute("Ratio_of_Integrands", pEvent->GetWeight());
        pHeadTiXmlElement->LinkEndChild(pTiXmlElement);
    }

    std::string fileName("/usera/sg568/PhysicsAnalysis/Generator/WhizardWeights/" + m_Process + "/" + m_Energy + "GeV/Reweighting_" + m_Process + "_" + m_Energy + "GeV_Alpha4_" + this->AlphasToString(m_Alpha4) + "_Alpha5_" + this->AlphasToString(m_Alpha5) + ".xml");

    bool success = tiXmlDocument.SaveFile(fileName.c_str());

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

template <class T>
std::string WeightToXmlConverter::AlphasToString(T Number)
{
    std::ostringstream ss;
    ss << std::fixed << std::setprecision(5) << Number;
    return ss.str();
}

//============================================================================

int main(int argc, char* argv[])
{
    std::string process("ee_nunuqqqq");
    std::string energy("1400");

    for (int i = -4; i < -2; i++)
    {
        for (int j = -4; j < -2; j++)
        {
            const float alpha4(i * 0.025);
            const float alpha5(j * 0.025);
            WeightToXmlConverter *pWeightToXmlConverter = new WeightToXmlConverter(process,energy,alpha4,alpha5);
        }
    } 
    return 0;
}
