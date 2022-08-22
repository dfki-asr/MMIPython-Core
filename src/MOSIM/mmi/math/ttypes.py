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

from thrift.transport import TTransport
all_structs = []


class MVector3(object):
    """
    Attributes:
     - X
     - Y
     - Z

    """


    def __init__(self, X=None, Y=None, Z=None,):
        self.X = X
        self.Y = Y
        self.Z = Z

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
                if ftype == TType.DOUBLE:
                    self.X = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.Y = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.Z = iprot.readDouble()
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
        oprot.writeStructBegin('MVector3')
        if self.X is not None:
            oprot.writeFieldBegin('X', TType.DOUBLE, 1)
            oprot.writeDouble(self.X)
            oprot.writeFieldEnd()
        if self.Y is not None:
            oprot.writeFieldBegin('Y', TType.DOUBLE, 2)
            oprot.writeDouble(self.Y)
            oprot.writeFieldEnd()
        if self.Z is not None:
            oprot.writeFieldBegin('Z', TType.DOUBLE, 3)
            oprot.writeDouble(self.Z)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.X is None:
            raise TProtocolException(message='Required field X is unset!')
        if self.Y is None:
            raise TProtocolException(message='Required field Y is unset!')
        if self.Z is None:
            raise TProtocolException(message='Required field Z is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MVector2(object):
    """
    Attributes:
     - X
     - Y

    """


    def __init__(self, X=None, Y=None,):
        self.X = X
        self.Y = Y

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
                if ftype == TType.DOUBLE:
                    self.X = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.Y = iprot.readDouble()
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
        oprot.writeStructBegin('MVector2')
        if self.X is not None:
            oprot.writeFieldBegin('X', TType.DOUBLE, 1)
            oprot.writeDouble(self.X)
            oprot.writeFieldEnd()
        if self.Y is not None:
            oprot.writeFieldBegin('Y', TType.DOUBLE, 2)
            oprot.writeDouble(self.Y)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.X is None:
            raise TProtocolException(message='Required field X is unset!')
        if self.Y is None:
            raise TProtocolException(message='Required field Y is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MQuaternion(object):
    """
    Attributes:
     - X
     - Y
     - Z
     - W

    """


    def __init__(self, X=None, Y=None, Z=None, W=None,):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.W = W

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
                if ftype == TType.DOUBLE:
                    self.X = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.Y = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.DOUBLE:
                    self.Z = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.W = iprot.readDouble()
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
        oprot.writeStructBegin('MQuaternion')
        if self.X is not None:
            oprot.writeFieldBegin('X', TType.DOUBLE, 1)
            oprot.writeDouble(self.X)
            oprot.writeFieldEnd()
        if self.Y is not None:
            oprot.writeFieldBegin('Y', TType.DOUBLE, 2)
            oprot.writeDouble(self.Y)
            oprot.writeFieldEnd()
        if self.Z is not None:
            oprot.writeFieldBegin('Z', TType.DOUBLE, 3)
            oprot.writeDouble(self.Z)
            oprot.writeFieldEnd()
        if self.W is not None:
            oprot.writeFieldBegin('W', TType.DOUBLE, 4)
            oprot.writeDouble(self.W)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.X is None:
            raise TProtocolException(message='Required field X is unset!')
        if self.Y is None:
            raise TProtocolException(message='Required field Y is unset!')
        if self.Z is None:
            raise TProtocolException(message='Required field Z is unset!')
        if self.W is None:
            raise TProtocolException(message='Required field W is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MVector(object):
    """
    Attributes:
     - Values

    """


    def __init__(self, Values=None,):
        self.Values = Values

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
                    self.Values = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readDouble()
                        self.Values.append(_elem5)
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
        oprot.writeStructBegin('MVector')
        if self.Values is not None:
            oprot.writeFieldBegin('Values', TType.LIST, 1)
            oprot.writeListBegin(TType.DOUBLE, len(self.Values))
            for iter6 in self.Values:
                oprot.writeDouble(iter6)
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


class MTransform(object):
    """
    Attributes:
     - ID
     - Position
     - Rotation
     - Scale
     - Parent

    """


    def __init__(self, ID=None, Position=None, Rotation=None, Scale=None, Parent=None,):
        self.ID = ID
        self.Position = Position
        self.Rotation = Rotation
        self.Scale = Scale
        self.Parent = Parent

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
                if ftype == TType.STRING:
                    self.ID = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.Position = MVector3()
                    self.Position.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.Rotation = MQuaternion()
                    self.Rotation.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.Scale = MVector3()
                    self.Scale.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.Parent = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('MTransform')
        if self.ID is not None:
            oprot.writeFieldBegin('ID', TType.STRING, 1)
            oprot.writeString(self.ID.encode('utf-8') if sys.version_info[0] == 2 else self.ID)
            oprot.writeFieldEnd()
        if self.Position is not None:
            oprot.writeFieldBegin('Position', TType.STRUCT, 2)
            self.Position.write(oprot)
            oprot.writeFieldEnd()
        if self.Rotation is not None:
            oprot.writeFieldBegin('Rotation', TType.STRUCT, 3)
            self.Rotation.write(oprot)
            oprot.writeFieldEnd()
        if self.Scale is not None:
            oprot.writeFieldBegin('Scale', TType.STRUCT, 4)
            self.Scale.write(oprot)
            oprot.writeFieldEnd()
        if self.Parent is not None:
            oprot.writeFieldBegin('Parent', TType.STRING, 5)
            oprot.writeString(self.Parent.encode('utf-8') if sys.version_info[0] == 2 else self.Parent)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.ID is None:
            raise TProtocolException(message='Required field ID is unset!')
        if self.Position is None:
            raise TProtocolException(message='Required field Position is unset!')
        if self.Rotation is None:
            raise TProtocolException(message='Required field Rotation is unset!')
        if self.Scale is None:
            raise TProtocolException(message='Required field Scale is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(MVector3)
MVector3.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'X', None, None, ),  # 1
    (2, TType.DOUBLE, 'Y', None, None, ),  # 2
    (3, TType.DOUBLE, 'Z', None, None, ),  # 3
)
all_structs.append(MVector2)
MVector2.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'X', None, None, ),  # 1
    (2, TType.DOUBLE, 'Y', None, None, ),  # 2
)
all_structs.append(MQuaternion)
MQuaternion.thrift_spec = (
    None,  # 0
    (1, TType.DOUBLE, 'X', None, None, ),  # 1
    (2, TType.DOUBLE, 'Y', None, None, ),  # 2
    (3, TType.DOUBLE, 'Z', None, None, ),  # 3
    (4, TType.DOUBLE, 'W', None, None, ),  # 4
)
all_structs.append(MVector)
MVector.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'Values', (TType.DOUBLE, None, False), None, ),  # 1
)
all_structs.append(MTransform)
MTransform.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'ID', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'Position', [MVector3, None], None, ),  # 2
    (3, TType.STRUCT, 'Rotation', [MQuaternion, None], None, ),  # 3
    (4, TType.STRUCT, 'Scale', [MVector3, None], None, ),  # 4
    (5, TType.STRING, 'Parent', 'UTF8', None, ),  # 5
)
fix_spec(all_structs)
del all_structs
