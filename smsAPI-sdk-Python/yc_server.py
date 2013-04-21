##################################################
# file: yc_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      C:\Python27\Scripts\wsdl2py-script.py http://114.80.200.100:8081/axis2/services/yc?wsdl
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from yc_types import *
from ZSI.ServiceContainer import ServiceSOAPBinding

# Messages  
getStatusByTimeRequest = GED("http://yc", "getStatusByTime").pyclass

getStatusByTimeResponse = GED("http://yc", "getStatusByTimeResponse").pyclass

mainRequest = GED("http://yc", "main").pyclass

getStatusByIdRequest = GED("http://yc", "getStatusById").pyclass

getStatusByIdResponse = GED("http://yc", "getStatusByIdResponse").pyclass

sendsmsRequest = GED("http://yc", "sendsms").pyclass

sendsmsResponse = GED("http://yc", "sendsmsResponse").pyclass

checkBalanceRequest = GED("http://yc", "checkBalance").pyclass

checkBalanceResponse = GED("http://yc", "checkBalanceResponse").pyclass

getReplyByTimeRequest = GED("http://yc", "getReplyByTime").pyclass

getReplyByTimeResponse = GED("http://yc", "getReplyByTimeResponse").pyclass


# Service Skeletons
class yc(ServiceSOAPBinding):
    soapAction = {}
    root = {}

    def __init__(self, post='/axis2/services/yc.ycHttpSoap11Endpoint/', **kw):
        ServiceSOAPBinding.__init__(self, post)

    def soap_getStatusByTime(self, ps, **kw):
        request = ps.Parse(getStatusByTimeRequest.typecode)
        return request, getStatusByTimeResponse()

    soapAction['urn:getStatusByTime'] = 'soap_getStatusByTime'
    root[(getStatusByTimeRequest.typecode.nspname, getStatusByTimeRequest.typecode.pname)] = 'soap_getStatusByTime'

    def soap_main(self, ps, **kw):
        request = ps.Parse(mainRequest.typecode)
        # NO output
        return request, None

    soapAction['urn:main'] = 'soap_main'
    root[(mainRequest.typecode.nspname, mainRequest.typecode.pname)] = 'soap_main'

    def soap_getStatusById(self, ps, **kw):
        request = ps.Parse(getStatusByIdRequest.typecode)
        return request, getStatusByIdResponse()

    soapAction['urn:getStatusById'] = 'soap_getStatusById'
    root[(getStatusByIdRequest.typecode.nspname, getStatusByIdRequest.typecode.pname)] = 'soap_getStatusById'

    def soap_sendsms(self, ps, **kw):
        request = ps.Parse(sendsmsRequest.typecode)
        return request, sendsmsResponse()

    soapAction['urn:sendsms'] = 'soap_sendsms'
    root[(sendsmsRequest.typecode.nspname, sendsmsRequest.typecode.pname)] = 'soap_sendsms'

    def soap_checkBalance(self, ps, **kw):
        request = ps.Parse(checkBalanceRequest.typecode)
        return request, checkBalanceResponse()

    soapAction['urn:checkBalance'] = 'soap_checkBalance'
    root[(checkBalanceRequest.typecode.nspname, checkBalanceRequest.typecode.pname)] = 'soap_checkBalance'

    def soap_getReplyByTime(self, ps, **kw):
        request = ps.Parse(getReplyByTimeRequest.typecode)
        return request, getReplyByTimeResponse()

    soapAction['urn:getReplyByTime'] = 'soap_getReplyByTime'
    root[(getReplyByTimeRequest.typecode.nspname, getReplyByTimeRequest.typecode.pname)] = 'soap_getReplyByTime'
