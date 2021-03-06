USE [master]
GO

CREATE DATABASE [ex9]
GO
ALTER DATABASE [ex9] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [ex9].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [ex9] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [ex9] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [ex9] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [ex9] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [ex9] SET ARITHABORT OFF 
GO
ALTER DATABASE [ex9] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [ex9] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [ex9] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [ex9] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [ex9] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [ex9] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [ex9] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [ex9] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [ex9] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [ex9] SET  DISABLE_BROKER 
GO
ALTER DATABASE [ex9] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [ex9] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [ex9] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [ex9] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [ex9] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [ex9] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [ex9] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [ex9] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [ex9] SET  MULTI_USER 
GO
ALTER DATABASE [ex9] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [ex9] SET DB_CHAINING OFF 
GO
ALTER DATABASE [ex9] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [ex9] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [ex9] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [ex9] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [ex9] SET QUERY_STORE = OFF
GO
USE [ex9]
GO
/****** Object:  Table [dbo].[FRIEND]    Script Date: 4/13/2022 21:37:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[FRIEND](
	[id] [int] NOT NULL,
	[senderid] [int] NOT NULL,
	[receiverid] [int] NOT NULL,
	[status] [varchar](50) NOT NULL,
	[createdtime] [timestamp] NOT NULL,
 CONSTRAINT [PK_FRIEND] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[message]    Script Date: 4/13/2022 21:37:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[message](
	[id] [int] NOT NULL,
	[senderid] [int] NOT NULL,
	[receiverid] [int] NOT NULL,
	[type] [varchar](50) NOT NULL,
	[content] [varchar](50) NULL,
	[status] [varchar](50) NULL,
	[createdtime] [datetime] NULL,
 CONSTRAINT [PK_message] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[USER_PROFILE]    Script Date: 4/13/2022 21:37:57 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[USER_PROFILE](
	[id] [int] NOT NULL,
	[username] [varchar](50) NOT NULL,
	[password] [varchar](50) NOT NULL,
	[fullname] [varchar](50) NOT NULL,
	[avatar] [varchar](50) NULL,
	[birthday] [datetime] NULL,
	[createdtime] [timestamp] NOT NULL,
 CONSTRAINT [PK_USER_PROFILE] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[FRIEND] ([id], [senderid], [receiverid], [status]) VALUES (1, 1, 1, N'pending')
INSERT [dbo].[FRIEND] ([id], [senderid], [receiverid], [status]) VALUES (2, 1, 2, N'accepted')
INSERT [dbo].[FRIEND] ([id], [senderid], [receiverid], [status]) VALUES (3, 2, 1, N'rejected')
INSERT [dbo].[FRIEND] ([id], [senderid], [receiverid], [status]) VALUES (4, 3, 3, N'accepted')
GO
INSERT [dbo].[message] ([id], [senderid], [receiverid], [type], [content], [status], [createdtime]) VALUES (1, 1, 2, N'text', N'linh', N'sent', CAST(N'2022-04-12T00:00:00.000' AS DateTime))
INSERT [dbo].[message] ([id], [senderid], [receiverid], [type], [content], [status], [createdtime]) VALUES (2, 2, 1, N'image', N'linh', N'sent', CAST(N'2022-04-13T00:00:00.000' AS DateTime))
INSERT [dbo].[message] ([id], [senderid], [receiverid], [type], [content], [status], [createdtime]) VALUES (3, 4, 4, N'video', N'linh', N'read', CAST(N'2022-04-12T00:00:00.000' AS DateTime))
INSERT [dbo].[message] ([id], [senderid], [receiverid], [type], [content], [status], [createdtime]) VALUES (4, 1, 1, N'text', N'linh vu', N'read', NULL)
GO
INSERT [dbo].[USER_PROFILE] ([id], [username], [password], [fullname], [avatar], [birthday]) VALUES (1, N'hnil', N'123', N'linh vu', N'123.jpg', CAST(N'2000-03-23T00:00:00.000' AS DateTime))
INSERT [dbo].[USER_PROFILE] ([id], [username], [password], [fullname], [avatar], [birthday]) VALUES (2, N'linh', N'123', N'vu linh', N'321.png', CAST(N'2000-04-21T00:00:00.000' AS DateTime))
INSERT [dbo].[USER_PROFILE] ([id], [username], [password], [fullname], [avatar], [birthday]) VALUES (3, N'nam', N'321', N'nam nguyen', N'2313.jpg', CAST(N'2000-04-12T00:00:00.000' AS DateTime))
INSERT [dbo].[USER_PROFILE] ([id], [username], [password], [fullname], [avatar], [birthday]) VALUES (4, N'nu', N'12131', N'nu vu', N'212312', CAST(N'2000-05-31T00:00:00.000' AS DateTime))
GO
USE [master]
GO
ALTER DATABASE [ex9] SET  READ_WRITE 
GO

Use ex9
go
--Lấy id, username, fullname, avatar: của các user có id =  2, 3. 

SELECT id, username, fullname, avatar FROM USER_PROFILE WHERE id = 2 or id =3

--Lấy các bạn bè(gồm thông tin sau: id, username, fullname, avatar) của user có id = 2.

