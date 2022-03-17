#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import MOSIM.mmi.services.MMIServiceBase
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(MOSIM.mmi.services.MMIServiceBase.Iface):
    def ApplyUpdates(self, sceneUpdates):
        """
        Parameters:
         - sceneUpdates

        """
        pass

    def ApplyManipulations(self, sceneManipulations):
        """
        Parameters:
         - sceneManipulations

        """
        pass


class Client(MOSIM.mmi.services.MMIServiceBase.Client, Iface):
    def __init__(self, iprot, oprot=None):
        MOSIM.mmi.services.MMIServiceBase.Client.__init__(self, iprot, oprot)

    def ApplyUpdates(self, sceneUpdates):
        """
        Parameters:
         - sceneUpdates

        """
        self.send_ApplyUpdates(sceneUpdates)
        return self.recv_ApplyUpdates()

    def send_ApplyUpdates(self, sceneUpdates):
        self._oprot.writeMessageBegin('ApplyUpdates', TMessageType.CALL, self._seqid)
        args = ApplyUpdates_args()
        args.sceneUpdates = sceneUpdates
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ApplyUpdates(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ApplyUpdates_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "ApplyUpdates failed: unknown result")

    def ApplyManipulations(self, sceneManipulations):
        """
        Parameters:
         - sceneManipulations

        """
        self.send_ApplyManipulations(sceneManipulations)
        return self.recv_ApplyManipulations()

    def send_ApplyManipulations(self, sceneManipulations):
        self._oprot.writeMessageBegin('ApplyManipulations', TMessageType.CALL, self._seqid)
        args = ApplyManipulations_args()
        args.sceneManipulations = sceneManipulations
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ApplyManipulations(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ApplyManipulations_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "ApplyManipulations failed: unknown result")


class Processor(MOSIM.mmi.services.MMIServiceBase.Processor, Iface, TProcessor):
    def __init__(self, handler):
        MOSIM.mmi.services.MMIServiceBase.Processor.__init__(self, handler)
        self._processMap["ApplyUpdates"] = Processor.process_ApplyUpdates
        self._processMap["ApplyManipulations"] = Processor.process_ApplyManipulations
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_ApplyUpdates(self, seqid, iprot, oprot):
        args = ApplyUpdates_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplyUpdates_result()
        try:
            result.success = self._handler.ApplyUpdates(args.sceneUpdates)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("ApplyUpdates", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_ApplyManipulations(self, seqid, iprot, oprot):
        args = ApplyManipulations_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplyManipulations_result()
        try:
            result.success = self._handler.ApplyManipulations(args.sceneManipulations)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("ApplyManipulations", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class ApplyUpdates_args(object):
    """
    Attributes:
     - sceneUpdates

    """


    def __init__(self, sceneUpdates=None,):
        self.sceneUpdates = sceneUpdates

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.sceneUpdates = MOSIM.mmi.scene.ttypes.MSceneUpdate()
                    self.sceneUpdates.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ApplyUpdates_args')
        if self.sceneUpdates is not None:
            oprot.writeFieldBegin('sceneUpdates', TType.STRUCT, 1)
            self.sceneUpdates.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ApplyUpdates_args)
ApplyUpdates_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'sceneUpdates', [MOSIM.mmi.scene.ttypes.MSceneUpdate, None], None, ),  # 1
)


class ApplyUpdates_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = MOSIM.mmi.core.ttypes.MBoolResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ApplyUpdates_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ApplyUpdates_result)
ApplyUpdates_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [MOSIM.mmi.core.ttypes.MBoolResponse, None], None, ),  # 0
)


class ApplyManipulations_args(object):
    """
    Attributes:
     - sceneManipulations

    """


    def __init__(self, sceneManipulations=None,):
        self.sceneManipulations = sceneManipulations

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.sceneManipulations = []
                    (_etype353, _size350) = iprot.readListBegin()
                    for _i354 in range(_size350):
                        _elem355 = MOSIM.mmi.scene.ttypes.MSceneManipulation()
                        _elem355.read(iprot)
                        self.sceneManipulations.append(_elem355)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ApplyManipulations_args')
        if self.sceneManipulations is not None:
            oprot.writeFieldBegin('sceneManipulations', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.sceneManipulations))
            for iter356 in self.sceneManipulations:
                iter356.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ApplyManipulations_args)
ApplyManipulations_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'sceneManipulations', (TType.STRUCT, [MOSIM.mmi.scene.ttypes.MSceneManipulation, None], False), None, ),  # 1
)


class ApplyManipulations_result(object):
    """
    Attributes:
     - success

    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = MOSIM.mmi.core.ttypes.MBoolResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ApplyManipulations_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ApplyManipulations_result)
ApplyManipulations_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [MOSIM.mmi.core.ttypes.MBoolResponse, None], None, ),  # 0
)
fix_spec(all_structs)
del all_structs

