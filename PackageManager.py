import eve.common.lib.appConst as const
import service
import uthread
import util
import blue
import log
import localization

class PackageManagerService(service.Service):
    __exportedcalls__ = {'GetCurrentRunningServices': [ROLE_ANY],
    'AddService': [ROLE_ANY],
    'RemoveService': [ROLE_ANY],
    'RunService': [ROLE_ANY],
    'StopService': [ROLE_ANY],
    'GetCurrentRunningMods': [ROLE_ANY],
    'EnableMod': [ROLE_ANY],
    'DisableMod': [ROLE_ANY],
    'GetModInstance': [ROLE_ANY],
    'GetServiceInstance': [ROLE_ANY],
    'DoRunOnceCode': [ROLE_ANY],
    'AddPackageFromFile': [ROLE_ANY],
    'GetServiceStatus': [ROLE_ANY],
    'GetOutputByInstance': [ROLE_ANY]
    }
    __guid__ = 'svc.packagemanager'
    __servicename__ = 'cpm'
    __displayname__ = 'Carbon Package Manager Service'
    #__notifyevents__ = ['OnSessionChanged']  ##Regist events here
    #__dependencies__ = []                    ##Declear dependencies here
    __update_on_reload__ = 1
    
    _Private_ServicesDictionary = []          ###This should be a dictionary
    _Private_ModThreadsDictionary = []        ###This should be a dictionary
    _Private_RunOnceCodeList = []
    
    def Run(self, ms):
        self.groupsQuotes = {}
        self.lastGotGroupsQuotes = {}
        self.lastGotGroupQuotes = {}
        self.groupQuotes = {}
        self.waitingFor = {}
        self.locks = {}
        self.orderCache = {}
        sm.FavourMe(self.OnOwnOrdersChanged)
    
    def GetCurrentRunningServices(self):
    
    def GetCurrentRunningMods(self):
    
    def AddService(self, sServiceName, sServiceSourceString):
    
    def AddPackageFromFile(self, sFileNameString):

    def RemoveService(self, sServiceName):
    
    def RunService(self, sServiceName):
    
    def StopService(self, sServiceName):
    
    def GetServiceStatus(self, sServiceName):
    
    def EnableMod(self, sModName, sModSourceString):
    
    def DisableMod(self, sModName):
    
    def GetModInstance(self, sModName):
    
    def GetServiceInstance(self, sServiceName):
    
    def DoRunOnceCode(self, sRunOnceCode):
    
    def GetOutputByInstance(self, instance)