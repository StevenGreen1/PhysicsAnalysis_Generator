#ifndef WEIGHT_TO_XML_CONVERTER_H
#define WEIGHT_TO_XML_CONVERTER_H

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>

#include "tinyxml.h"

using namespace std;

enum SuccessEnum {FAILURE, SUCCESS};

class WeightToXmlConverter
{
    public:
        WeightToXmlConverter();

        ~WeightToXmlConverter();

    private:
        void LoadASCII();

        void SaveXml();

        template <class T>
        std::string FileNumberToString(T Number);

        class Event
        {
            private:
                int m_EventNumber;
                float m_Alpha4;
                float m_Alpha5;
                float m_Weight;
            public:
                void SetEventNumber(int eventNumber) { m_EventNumber = eventNumber; }
                void SetAlpha4(float alpha4) { m_Alpha4 = alpha4; }
                void SetAlpha5(float alpha5) { m_Alpha5 = alpha5; }
                void SetWeight(float weight) { m_Weight = weight; }
                int GetEventNumber() { return m_EventNumber; }
                float GetAlpha4() { return m_Alpha4; }
                float GetAlpha5() { return m_Alpha5; }
                float GetWeight() { return m_Weight; }
        };

        typedef std::vector<WeightToXmlConverter::Event*> EventVector;
        EventVector m_Events;
};

#endif
